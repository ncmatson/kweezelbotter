#include "chunk.h"

Chunk::Chunk() : Element("", 0) {}

Chunk::Chunk(std::string name) : Element(name, 1) {}

Chunk::~Chunk() {}

std::string Chunk::getName() {
  return Element::getKey();
}

int Chunk::getFrequency() {
  return Element::getValue();
}
