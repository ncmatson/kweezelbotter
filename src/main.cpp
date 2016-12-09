/* Kweezelbotter is a pronunciation tool to pronounce
 * words like Kweezelbotter.
 *
 * Cameron Matson
 * Clayton Gentry
 * 2016
 */

#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>


#define DICTIONARY_FILE "dict/dict.txt"

void loadTrainingSet(std::string fileName, std::vector<std::string>& words, std::vector<std::string>& pronunciations){
  std::ifstream file(fileName);

  if (file) {
    std::string line;

    while (std::getline(file,line)) {
      if (line.substr(0,3) == ";;;") {
        continue;
      }
      else {
        std::string word;
        std::string pronunciation;
        std::istringstream ss(line);

        //add word to *words*
        ss >> word;
        words.push_back(word);

        //add pronunciation to *pronunciations*
        while (ss >> pronunciation) pronunciation += pronunciation + " ";
        pronunciations.push_back(pronunciation);
      }
    }
  }
  else {
    std::cerr << "Unable to load dictionary" << std::endl;
  }
}

int main() {
  std::vector<std::string> words;
  std::vector<std::string> pronunciations;

  loadTrainingSet(DICTIONARY_FILE,words,pronunciations);

}
