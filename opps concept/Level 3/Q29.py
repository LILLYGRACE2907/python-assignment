# Question 29
# Create a FoodOrder class and a DeliveryService class. Make the food order USE-A the delivery service.

class DeliveryService:
    def deliver(self, name):
        print("DeliveryService:", name)

class FoodOrder:
    def __init__(self, name):
        self.name = name

    def use_service(self, service):
        service.deliver(self.name)

obj = FoodOrder("Example")
obj.use_service(DeliveryService())
