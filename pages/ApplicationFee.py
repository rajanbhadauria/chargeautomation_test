import stripe
stripe.api_key = ""


class ApplicationFee:

    def getCustomers(self, limitcount=1):
        customers = stripe.Customer.list(limit=limitcount)
        for customer in customers["data"]:
            print(customer['email'])

    def getPaymentIntents(self, limitcount = 1):
        payment_intents = stripe.PaymentIntent.list(limit=limitcount)
        for payment_intent in payment_intents["data"]:
            print(payment_intent)


appFee = ApplicationFee()
appFee.getPaymentIntents(10)

