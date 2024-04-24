    std::string intToBinary(int number) {
        return std::bitset<32>(number).to_string();
    }
