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


#define DICTIONARY_FILE "dict/dict.txt"

/* splits the given string along the delimiter patern */
std::vector<std::string> split(const std::string& str, char delim) {
  std::vector<std::string> result;
  std::stringstream ss(str);
  std::string token;

  while(std::getline(ss,token,delim)) {
    result.push_back(token);
  }

  return result;
}

//TODO: too many big chunks
std::vector<std::string> chunk(const std::string& str, int num) {
  std::vector<std::string> result;

  //put one letter in each chunk until you only have one chunk left to fill
  int i;
  for (i = 0; i < str.length() && i < (num-1); ++i) {
    std::string s(1,str[i]);
    result.push_back(s);
  }

  //fill the last chunk wih the rest of the string
  if (i < str.length()) { result.push_back(str.substr(i)); }
  if (result[result.size()-1].length() > 2) bigChunks++;

  return result;
}

void loadTrainingSet( std::string fileName,
                      std::vector<std::vector<std::string>>& words,
                      std::vector<std::vector<std::string>>& pronunciations){

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

        std::vector<std::string> chunks;
        std::vector<std::string> phonemes;

        std::stringstream ss(line);

        //pick off word
        ss >> word;

        //pick of pronunciation
        ss.get();
        std::getline(ss, pronunciation);
        pronunciation = pronunciation.substr(1);

        //split phonemes
        phonemes = split(pronunciation, ' ');

        //chunk word s.t. the number of chunks = number of phonemes
        chunks = chunk(word, phonemes.size());

        pronunciations.push_back(phonemes);
        words.push_back(chunks);
      }
    }
  }
  else {
    std::cerr << "Unable to load dictionary" << std::endl;
  }
}


int main() {
  std::vector<std::vector<std::string>> words;
  std::vector<std::vector<std::string>> pronunciations;

  loadTrainingSet(DICTIONARY_FILE,words,pronunciations);

}
