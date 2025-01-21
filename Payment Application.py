from flask import Flask, render_template, request, jsonify
import stripe
import os

# Initialize Flask app
app = Flask(__name__)

# Stripe API keys (replace with your keys)
stripe.api_key = "your_secret_key"

# Routes
@app.route("/")
def home():
    """Render the payment page."""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Payment Application</title>
        <script src="https://js.stripe.com/v3/"></script>
        <style>
            body { font-family: Arial, sans-serif; margin: 50px; }
            #payment-form { max-width: 400px; margin: auto; }
            #card-element { border: 1px solid #ccc; padding: 10px; border-radius: 5px; margin-bottom: 20px; }
            button { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>Payment Application</h1>
        <form id="payment-form">
            <input type="text" id="card-holder-name" placeholder="Cardholder Name" required><br><br>
            <div id="card-element"></div>
            <button id="submit">Pay</button>
        </form>
        <script>
            const stripe = Stripe("your_publishable_key");
            const elements = stripe.elements();
            const cardElement = elements.create("card");
            cardElement.mount("#card-element");

            const form = document.getElementById("payment-form");
            form.addEventListener("submit", async (event) => {
                event.preventDefault();
                const { paymentIntent, error } = await stripe.confirmCardPayment(
                    await fetch("/create-payment-intent", { method: "POST" }).then(res => res.json()).then(data => data.clientSecret),
                    {
                        payment_method: {
                            card: cardElement,
                            billing_details: {
                                name: document.getElementById("card-holder-name").value,
                            },
                        },
                    }
                );

                if (error) {
                    alert(`Payment failed: ${error.message}`);
                } else {
                    alert("Payment succeeded!");
                }
            });
        </script>
    </body>
    </html>
    '''

@app.route("/create-payment-intent", methods=["POST"])
def create_payment_intent():
    """Create a payment intent for Stripe."""
    try:
        # Fixed amount (e.g., $10.00)
        amount = 1000  # Amount in cents

        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="usd",
            payment_method_types=["card"],
        )
        return jsonify({"clientSecret": payment_intent["client_secret"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    # Set environment variable for development
    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)
