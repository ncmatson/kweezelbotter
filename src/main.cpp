/* Kweezelbotter is a pronunciation tool to pronounce
 * words like Kweezelbotter.
 *
 * Cameron Matson
 * Clayton Gentry
 * 2016
 */

#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

#include "chunkModel.h"

#define DICTIONARY_FILE "dict/dict.txt"

void loadTrainingSet( std::string fileName, ChunkModel* cm){
  std::ifstream file(fileName);

  if (file) {
    std::string line;

    while (std::getline(file,line)) {
      if (line.substr(0,3) == ";;;") {
        continue;
      }
      else {
        cm->addLine(line);
      }
    }
  }
  else {
    std::cerr << "Unable to load dictionary" << std::endl;
  }
}

int main() {

  ChunkModel* cm = new ChunkModel();

  loadTrainingSet(DICTIONARY_FILE, cm);

  std::cout<<cm->getSize()<<std::endl;
  cm->printSizes();

  std::cout<<cm->getMax()<<std::endl;

  cm->print("data/matrix.txt");
}
