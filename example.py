from payping import payping

pay = payping("USERNAME") # https://www.payping.ir/{USERNAME} its your username

payment_url = pay.PaymentRequest(2000, "Paye Name", "Paye Description")

print("your payment: ", payment_url)

verify = pay.PaymentVerify(payment_url)

print("paid ?: ", verify)
