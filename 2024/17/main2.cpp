#include <cassert>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <string>
#include <sys/socket.h>
#include <sys/types.h>
#include <vector>

size_t registers[3];
std::vector<uint8_t> program;
std::vector<uint8_t> output;
uint8_t pc = 0;

size_t operand(uint8_t o) {
  assert(o != 7);
  if (o <= 3) {
    return o;
  }
  return registers[o - 4];
}

void adv(uint8_t o) {
  size_t numerator = registers[0];
  size_t denominator = 1 << operand(o);
  size_t result = numerator / denominator;
  registers[0] = result;
  pc += 2;
}

void bxl(uint8_t o) {
  size_t result = registers[1] ^ o;
  registers[1] = result;
  pc += 2;
}

void bst(uint8_t o) {
  size_t result = operand(o) & 0b111;
  registers[1] = result;
  pc += 2;
}

void jnz(uint8_t o) {
  if (registers[0] == 0) {
    pc += 2;
    return;
  }
  pc = o;
}

void bxc(uint8_t o) {
  size_t result = registers[1] ^ registers[2];
  registers[1] = result;
  pc += 2;
}

void out(uint8_t o) {
  size_t result = operand(o) & 0b111;
  output.push_back(result);
  pc += 2;
}

void bdv(uint8_t o) {
  size_t numerator = registers[0];
  size_t denominator = 1 << operand(o);
  size_t result = numerator / denominator;
  registers[1] = result;
  pc += 2;
}

void cdv(uint8_t o) {
  size_t numerator = registers[0];
  size_t denominator = 1 << operand(o);
  size_t result = numerator / denominator;
  registers[2] = result;
  pc += 2;
}

bool check_quiune() {
  if (program.size() != output.size())
    return false;

  for (uint8_t i = 0; i < program.size(); i++) {
    if (program[i] != output[i])
      return false;
  }
  return true;
}

int main() {
  std::ifstream inputFile("input.txt");
  std::string line;
  for (uint i = 0; i < 3; i++) {
    std::getline(inputFile, line);
    size_t idx = line.find(":") + 1;
    registers[i] = std::stoi(line.substr(idx));
  }

  std::getline(inputFile, line);
  std::getline(inputFile, line);
  for (size_t pos = 9; pos < line.length(); pos += 2) {
    program.push_back(line[pos] - '0');
  }

  size_t a = 0;
  while (!check_quiune()) {
    registers[0] = a++;
    registers[1] = 0;
    registers[2] = 0;
    pc = 0;
    output.clear();
    printf("%lu\n", a);
    while (pc < program.size()) {
      switch (program[pc]) {
      case 0:
        adv(program[pc + 1]);
        break;
      case 1:
        bxl(program[pc + 1]);
        break;
      case 2:
        bst(program[pc + 1]);
        break;
      case 3:
        jnz(program[pc + 1]);
        break;
      case 4:
        bxc(program[pc + 1]);
        break;
      case 5:
        out(program[pc + 1]);
        if (program[output.size() - 1] != output[output.size() - 1])
          continue;
        break;
      case 6:
        bdv(program[pc + 1]);
        break;
      case 7:
        cdv(program[pc + 1]);
        break;
      }
    }
  }
  printf("%lu\n", a);
}
