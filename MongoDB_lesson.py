import json
import pymongo

client = pymongo.MongoClient()
db = client.scouting_system
match_data = db.match_data

with open("example_tim_data.json") as f:
    data = json.loads(f.read())


class Team:
    def __init__(self, team_number, data):
        self.team_number = team_number
        TIM = []
        for match in data:
            if match["team_num"] == team_number:
                TIM.append(match)

        self.TIM = TIM

    def average_balls_scored(self):
        average_balls_scored = 0
        count = 0
        for match in self.TIM:
            average_balls_scored += match["num_balls"]
            count += 1

        avg_balls_scored = average_balls_scored / count
        return avg_balls_scored

    def fewest_balls_scored(self):
        fewest_balls_scored = 10000000
        for match in self.TIM:
            if match["num_balls"] < fewest_balls_scored:
                fewest_balls_scored = match["num_balls"]
        return fewest_balls_scored

    def most_balls_scored(self):
        most_balls_scored = 0
        for match in self.TIM:
            if match["num_balls"] > most_balls_scored:
                most_balls_scored = match["num_balls"]
        return most_balls_scored

    def number_of_matches_played(self):
        self.number_of_matches_played = len(self.TIM)
        return self.number_of_matches_played

    def percent_climb_success(self):
        climbed = 0
        for match in self.TIM:
            if match["climbed"]:
                climbed += 1

        percent_climb_success = (climbed / self.number_of_matches_played) * 100
        return percent_climb_success


test = Team(429, data)
processed_data = {"average_balls_scored": test.average_balls_scored(),
                  "fewest_balls_scored": test.fewest_balls_scored(), "most_balls_scored": test.most_balls_scored(),
                  "number_of_matches_played": test.number_of_matches_played(),
                  "percent_climb_success": test.percent_climb_success()}

TEST_id = match_data.insert_one(processed_data).inserted_id


