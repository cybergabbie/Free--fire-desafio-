import random
import time

class FreeFireGame:
    def __init__(self, num_players=10, map_size=20):
        self.map_size = map_size
        self.players = [{'id': i, 'x': random.randint(0, map_size-1), 'y': random.randint(0, map_size-1), 'health': 100, 'weapon': 'fist'} for i in range(num_players)]
        self.items = [{'x': random.randint(0, map_size-1), 'y': random.randint(0, map_size-1), 'type': 'weapon'} for _ in range(5)]
        self.storm_radius = map_size // 2
        self.storm_center = (map_size // 2, map_size // 2)

    def distance(self, p1, p2):
        return abs(p1['x'] - p2['x']) + abs(p1['y'] - p2['y'])

    def in_storm(self, player):
        dist = self.distance(player, {'x': self.storm_center[0], 'y': self.storm_center[1]})
        return dist > self.storm_radius

    def move_player(self, player):
        player['x'] = max(0, min(self.map_size-1, player['x'] + random.choice([-1, 0, 1])))
        player['y'] = max(0, min(self.map_size-1, player['y'] + random.choice([-1, 0, 1])))

    def collect_item(self, player):
        for item in self.items[:]:
            if player['x'] == item['x'] and player['y'] == item['y']:
                player['weapon'] = 'rifle'  # Upgrade
                self.items.remove(item)

    def combat(self):
        for i, p1 in enumerate(self.players):
            for j, p2 in enumerate(self.players):
                if i != j and self.distance(p1, p2) <= 1 and p1['health'] > 0 and p2['health'] > 0:
                    p2['health'] -= 20  # Ataque simples

    def update_storm(self):
        self.storm_radius = max(1, self.storm_radius - 1)
        for player in self.players:
            if self.in_storm(player):
                player['health'] -= 10

    def remove_dead(self):
        self.players = [p for p in self.players if p['health'] > 0]

    def run(self):
        while len(self.players) > 1:
            for player in self.players:
                self.move_player(player)
                self.collect_item(player)
            self.combat()
            self.update_storm()
            self.remove_dead()
            self.print_status()
            time.sleep(1)
        print(f"Vencedor: Jogador {self.players[0]['id']}")

    def print_status(self):
        print(f"Jogadores vivos: {len(self.players)}, Raio da zona: {self.storm_radius}")
        # Opcional: Imprima mapa simples

game = FreeFireGame()
game.run()
