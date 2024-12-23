#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
#define W 71
#define H 71

struct Pos {
	uint8_t x, y;
	bool operator==(const Pos &other) const {
		return x == other.x && y == other.y;
	}
	bool operator<(const Pos &other) const {
		return std::tie(x, y) < std::tie(other.x, other.y);
	}
};

char grid[H][W];
std::vector<Pos> incoming;

void init_grid() {
	for (uint8_t y = 0; y < H; y++) {
		for (uint8_t x = 0; x < W; x++) {
			grid[y][x] = '.';
		}
	}
}

size_t byte_idx = 0;
void drop_byte() {
	auto pos = incoming[byte_idx++];
	grid[pos.y][pos.x] = '#';
}

void drop_n_bytes(size_t n) {
	for (size_t i = 0; i < n; i++) {
		drop_byte();
	}
}

void parse_input() {
	std::ifstream inputFile("input.txt");
	std::string line;
	while (std::getline(inputFile, line)) {
		std::stringstream iss(line);
		std::string token;
		int a, b;
		std::getline(iss, token, ',');
		a = std::stoi(token);
		std::getline(iss, token, ',');
		b = std::stoi(token);
		incoming.emplace_back(a, b);
	}
}

void draw() {
	for (const auto &row : grid) {
		for (const auto &c : row) {
			std::cout << c << " ";
		}
		std::cout << '\n';
	}
}

struct Node {
	uint8_t x, y;
	int f, g, h;
	Pos parent;

	Node(uint8_t x, uint8_t y, int g, int h, Pos parent)
	: x(x), y(y), g(g), h(h), parent(parent) {
		f = g + h;
	}

	bool operator>(const Node &other) const { return f > other.f; }
};

int manhattan_distance(uint8_t x1, uint8_t y1, uint8_t x2, uint8_t y2) {
	return std::abs(x1 - x2) + std::abs(y1 - y2);
}

std::vector<Pos> Astar(Pos start, Pos goal) {
	std::priority_queue<Node, std::vector<Node>, std::greater<Node>> open_set;
	std::map<Pos, Pos> came_from;
	std::map<Pos, int> g_score;

	open_set.push(Node(start.x, start.y, 0,
					manhattan_distance(start.x, start.y, goal.x, goal.y),
					start));
	g_score[start] = 0;

	const int dx[] = {0, 1, 0, -1};
	const int dy[] = {-1, 0, 1, 0};

	while (!open_set.empty()) {
		Node current = open_set.top();
		open_set.pop();

		Pos current_pos = {current.x, current.y};

		if (current_pos == goal) {
			std::vector<Pos> path;
			while (current_pos != start) {
				path.push_back(current_pos);
				current_pos = came_from[current_pos];
			}
			path.push_back(start);
			std::reverse(path.begin(), path.end());
			return path;
		}

		for (int i = 0; i < 4; i++) {
			uint8_t new_x = current.x + dx[i];
			uint8_t new_y = current.y + dy[i];
			Pos neighbor = {new_x, new_y};

			if (new_x >= W || new_y >= H)
				continue;

			if (grid[new_y][new_x] == '#')
				continue;

			int tentative_g = g_score[current_pos] + 1;

			if (!g_score.count(neighbor) || tentative_g < g_score[neighbor]) {
				came_from[neighbor] = current_pos;
				g_score[neighbor] = tentative_g;

				int h = manhattan_distance(new_x, new_y, goal.x, goal.y);
				open_set.push(Node(new_x, new_y, tentative_g, h, current_pos));
			}
		}
	}

	return std::vector<Pos>();
}

int main() {
	parse_input();
	init_grid();
	drop_n_bytes(1024);
	draw();
	auto path = Astar({0, 0}, {W - 1, H - 1});
	printf("%lu\n", path.size() - 1);

	while(path.size() > 0) {
		drop_byte();
		path = Astar({0, 0}, {W - 1, H - 1});
	}
	Pos last = incoming[byte_idx-1];
	printf("%d,%d\n", last.x, last.y);
}
