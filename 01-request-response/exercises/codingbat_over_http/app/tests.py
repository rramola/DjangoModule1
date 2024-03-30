from django.test import SimpleTestCase


class TestWarmupOne(SimpleTestCase):
    def near_hundred_one(self):
        response = self.client.get("/warmup-one/93")
        self.assertContains(response, True)

    def near_hundred_two(self):
        response = self.client.get("/warmup-one/90")
        self.assertContains(response, True)

    def near_hundred_three(self):
        response = self.client.get("/warmup-one/89")
        self.assertContains(response, False)


class TestWarmupTwoView(SimpleTestCase):
    def string_splosion_one(self):
        response = self.client.get("/warmup-two/Code")
        self.assertContains(response, "CCoCodCode")

    def string_splosion_two(self):
        response = self.client.get("/warmup-two/abc")
        self.assertContains(response, "aababc")

    def string_splosion_three(self):
        response = self.client.get("/warmup-two/ab")
        self.assertContains(response, "aab")


class TestWarmUpThreeView(SimpleTestCase):
    def cat_dog_one(self):
        response = self.client.get("/cat-dog/catdog")
        self.assertContains(response, True)

    def cat_dog_two(self):
        response = self.client.get("/cat-dog/catcat")
        self.assertContains(response, False)

    def cat_dog_three(self):
        response = self.client.get("/cat-dog/1cat1cadodog")
        self.assertContains(response, True)


class TestWarmupFourView(SimpleTestCase):
    def lone_sum_one(self):
        response = self.client.get("/lone-sum/1/2/3")
        self.assertContains(response, 6)

    def lone_sum_two(self):
        response = self.client.get("/lone-sum/3/2/3")
        self.assertContains(response, 2)

    def lone_sum_three(self):
        response = self.client.get("/lone-sum/3/3/3")
        self.assertContains(response, 0)
