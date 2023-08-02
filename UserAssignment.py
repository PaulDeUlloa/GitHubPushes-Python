class User:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.email}")
        print(f"{self.age}")

    def enroll(self):
        print(f"Member staus is {self.is_rewards_member} and your total points is {self.gold_card_points}")

    def spend_points(self,amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount

Paul = User("Paul","De Ulloa","Pauld@CodingDojo.com",26)
Joe = User("Joe","Doodle","Joed@CodingDojo.com",62)

Paul.is_rewards_member = (True)
Paul.gold_card_points = (200)

Paul.spend_points(50)
Paul.display_info()
Paul.enroll()

Joe.is_rewards_member = (True)
Joe.gold_card_points = (200)

Joe.spend_points(80)
Joe.display_info()
Joe.enroll()