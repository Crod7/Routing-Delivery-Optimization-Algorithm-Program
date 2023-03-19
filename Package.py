class Package:
    def __init__(self, id, address, city, state, zipCode, deadline, deliveryStatus, weight):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.deliveryStatus = deliveryStatus
        self.state = state
        self.city = city
        self.zipCode = zipCode
        self.weight = weight

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" %(self.id, self.address, self.city, self.state, self.zipCode, self.zipCode, self.deadline, self.deliveryStatus, self.weight)
