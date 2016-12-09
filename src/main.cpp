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
        std::string buff;
        std::stringstream ss(line);

        //add word to *words*
        ss >> word;
        words.push_back(word);

        //add pronunciation to *pronunciations*
        ss.get();
        std::getline(ss, pronunciation);
        //while(ss >> buff) pronunciation += pronunciation + "|";
        pronunciations.push_back(pronunciation.substr(1));
      }
    }
  }
  else {
    std::cerr << "Unable to load dictionary" << std::endl;
  }
}

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

std::vector<std::string> chunk(const std::string& str, int num) {
  std::vector<std::string> result;
  int i;

  //put one letter in each chunk until you only have one chunk left to fill
  for (i = 0; i < str.length() && result.size() < (num-1); ++i) {
    std::string s(1,str[i]);
    result.push_back(s);
  }

  //fill the last chunk wih the rest of the string
  if (i < str.length()) { result.push_back(str.substr(i)); }

  for (int j = 0; j < result.size(); ++j) {
    std::cout<<result[j]<<std::endl;
  }

  return result;
}


int main() {
  std::vector<std::string> words;
  std::vector<std::string> pronunciations;

  std::string gravy("gravy");

  std::vector<std::string> s = chunk(gravy,-1);

  loadTrainingSet(DICTIONARY_FILE,words,pronunciations);

}
