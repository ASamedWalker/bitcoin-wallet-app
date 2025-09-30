# app.py
import os
from flask import Flask, request, jsonify, redirect
import requests

# ---- Config (use env vars; never hardcode secrets) ----
BTCPAY_URL = os.getenv("BTCPAY_URL", "https://testnet.demo.btcpayserver.org")
STORE_ID = os.getenv("BTCPAY_STORE_ID", "REPLACE_ME")
API_KEY = os.getenv("BTCPAY_API_KEY", "REPLACE_ME")

app = Flask(__name__)


def create_invoice(amount, currency="USD", order_id="ABC123"):
    url = f"{BTCPAY_URL}/api/v1/stores/{STORE_ID}/invoices"
    headers = {"Authorization": f"token {API_KEY}", "Content-Type": "application/json"}
    data = {
        "amount": f"{float(amount):.2f}",
        "currency": currency,
        "metadata": {"orderId": order_id},
        "checkout": {"speedPolicy": "HighSpeed"},
    }
    r = requests.post(url, headers=headers, json=data, timeout=20)
    r.raise_for_status()
    return r.json()


@app.route("/")
def index():
    return (
        "<h1>Bitcoin Payments (BTCPay)</h1>"
        "<p>Try <a href='/create-invoice?amount=19.99&currency=USD&order_id=ORDER-123'>Create Invoice</a></p>"
        "<p>Webhook endpoint: <code>/webhook/btcpay</code> (POST)</p>"
    )


@app.route("/create-invoice")
def create_invoice_route():
    amount = request.args.get("amount", "1.00")
    currency = request.args.get("currency", "USD")
    order_id = request.args.get("order_id", "ABC123")

    try:
        invoice = create_invoice(amount, currency, order_id)
        checkout = invoice.get("checkoutLink")
        if not checkout:
            return (
                jsonify({"error": "No checkoutLink in response", "invoice": invoice}),
                502,
            )
        # Redirect user to BTCPay's hosted checkout page (QR / on-chain / Lightning)
        return redirect(checkout, code=302)
    except requests.HTTPError as e:
        return (
            jsonify(
                {
                    "error": "BTCPay API error",
                    "detail": str(e),
                    "body": getattr(e.response, "text", ""),
                }
            ),
            502,
        )
    except Exception as e:
        return jsonify({"error": "Unexpected error", "detail": str(e)}), 500


@app.route("/webhook/btcpay", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    # TODO: verify HMAC signature if you set a webhook secret in BTCPay
    # Example fields: data['invoiceId'], data['status'], data.get('metadata', {}).get('orderId')
    print("Webhook received:", data)
    # Update your order status in DB here based on data['status'] (New/Processing/Settled/Expired)
    return jsonify({"ok": True})


if __name__ == "__main__":
    # For dev only; use a proper WSGI server in prod
    app.run(host="127.0.0.1", port=5000, debug=True)
