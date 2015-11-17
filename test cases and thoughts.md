base case questions:
  1. how long does it take to learn up to a given value?
  2. how accurate does it learn to?

alternate things:
1. interrupt a half-trained base case network, use that as the starting case of a network, see how long it takes to train from there
2. figure out a simple kind of idea for a more fundamental kind of data (like edges) and train a thinner network on that data. then use that network as the first layer of a thicker network. see how much faster that learns than one that starts with randoms
3. take out a vertical slice (incomplete pieces out of several layers) and transplant it into another network
4. train a neural network on different data and then see how it compares
5. take something with known classification, and transplant individual sets of neurons - for example, in that one article on the unreasonable effectiveness of RNNs, he found some neurons that fired when the net was inside a set of parentheses; try extracting just that neuron, and the neurons that contribute to it, and seeding those into a network to start. how does that learning compare to the base case?
6. watch a network as we're training it. if we see a neuron that fires in a certain condition, manually nuke it.
7. find neurons that are used less than a certain amount, and zero them out. note: "used less than a certain amount" could mean "is only used very weakly" and it could mean "close to being a linear combination of other neurons"
8. take us down to reduced row echelon form or something? to figure out if neurons are independant

i guess a relevant useful tool would be to select a set of input training cases and give a listing of neurons that are correlated with those training cases (as in the RNN post)

play around with an "unknown" output neuron in addition to classifiers

how can you make a neural network output data structures, like, could you make a neural network that would be even *capable* of producing like, an AST. whatever the solution is its gonna involve training on really simple cases i guess

using neural networks to train neural networks??
