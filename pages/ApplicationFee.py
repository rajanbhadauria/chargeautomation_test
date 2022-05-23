import stripe
#stripe.api_key = "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"
stripe.api_key = "sk_test_T0j6EMKsMwikJbictYjr9rBb"


class ApplicationFee:

    def getCustomers(self, limitcount=1):
        customers = stripe.Customer.list(limit=limitcount)
        for customer in customers["data"]:
            print(customer['email'])

    def getPaymentIntents(self, limitcount = 1):
        payment_intents = stripe.PaymentIntent.list(stripe_account="acct_1KrJK1IjChgILC9D", limit=limitcount)
        for payment_intent in payment_intents["data"]:
            if payment_intent["application_fee_amount"]:
                #print(self.getAppFee(payment_intent["charges"]["data"][0]['application_fee']))
                print(payment_intent["charges"]["data"][0])

    def getAppFee(self, app_fee_ref):
        if app_fee_ref:
            return stripe.ApplicationFee.retrieve(app_fee_ref)

    def getAllTxns(self, limitcount = 1):
        txns = stripe.issuing.Transaction.list(limit=limitcount)
        for txn in txns["data"]:
            print(txn["application_fee"])

    def getAllCharges(self, limitcount = 1):
        charges = stripe.BalanceTransaction.list(limit=limitcount)
        for charge in charges["data"]:
            print(charge)

    def getAllCustomerTxn(self, limitcount=1):
        charges = stripe.Customer.list_balance_transactions("cus_CtpAQ8qEpTUJLh", limit=limitcount)
        print(charges)
        for charge in charges:
            print(charge)

    def getInvoices(self, limitcount=1):
        charges = stripe.Customer.list_balance_transactions("cus_CtpAQ8qEpTUJLh", limit=limitcount)
        print(charges)
        for charge in charges:
            print(charge)


appFee = ApplicationFee()
appFee.getPaymentIntents(10)

