# Compiler and options
CXX := g++
CXXFLAGS := -std=c++20

# Target binary
TARGET := hello

# Source files
SRCS := main2.cpp

# Build and run
all: $(TARGET)
	./$(TARGET)

# Compile the target
$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) $< -o $@

# Clean the build
clean:
	rm -f $(TARGET)

