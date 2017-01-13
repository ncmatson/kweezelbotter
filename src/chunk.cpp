#include "chunk.h"
#include <iostream>
Chunk::Chunk() : Element("", 0) {}

Chunk::Chunk(std::string name) : Element(name, 0) {}

Chunk::~Chunk() {}

std::string Chunk::getName() {
  return Element::getKey();
}

int Chunk::getFrequency() {
  return Element::getValue();
}

void Chunk::incrementFrequency() {
  value++;
}
