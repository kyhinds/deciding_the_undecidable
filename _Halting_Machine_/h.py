from math import sin, cos, tan, atan, exp, pi
# Project Name: "Deciding the Undecidable"
# Author: Kyle Hinds
# Date: April 20th, 2024
# Terms of Use:
# This software is provided 'as-is', without warranty.
# If you find this interesting or useful in any way, feel free to make a $BTC donation to 'bc1pfxhfmalgpl3v2nq9nx37w4320635dr5x587rh74klzew3gyqv47qtnpaev'.
# Donations are appreciated and will contribute towards future research in computer science.
# Code contributions are also welcome and fall under the same terms.
# Not a legal contract.
"""
# Here, we offer a solution to Alan Turing's Halting Problem (Turing, 1936), properly defining and algebraically modeling the Turing Machines H and Q.
# In the paper "Deciding The Undecidable" (Hinds, 2024), we demonstrated how and why Q must have an input.
# Turing machines are finite computational models that process finite strings of input, executing operations based on a finite set of rules.
# In the Halting Problem, H(P,I) tells us if P(I) halts or loops forever, while Q(P) loops forever if H(P,P) returns 'halt', or halts if H(P,P) returns 'loop'.
# We propose that Q(null) loops because H(null,null) = 'halt' on no input, and with Q behaving opposite of H, Q(null) loops forever.
# The hypothetical paradox of H(Q,Q) predicting both looping and halting simultaneously fails to acknowledge the base case for Q.
# If we let P = Q and I = Q, the inner Q will have no input, giving us H(Q,Q(null)).
# Evaluating this we get H(Q,loop) = H(Q(loop)) = 'halt'.
# With a simple proof by induction on Q: Base: Q(null) loops, Step: Q(Q)='halt' and Next: Q(Q(Q)) loops returning to the base case.
# In general, this recursive Q function loops if for the number of iterations, n, satisfies (n mod 2) ≡ 0 (even).
# Conversely, it halts for an odd number of iterations, where (n mod 2) ≡ 1 (odd).
# Failing to require a base case leads to the infinite input string Q(Q(...(Q))) = Q∞ = Qω.
# In set theory, ∞ is represented by the ordinal ω with cardinality ℵ₀, and ω is even if ∃β such that 2β = α.
# With ordinal arithmetic, 2⋅ω = ω, but ω + 1 > ω, so ω can be seen as an infinite series of pairs, making it even.
# This satisfies the even definition with β as ω itself, showcasing its transfinite evenness.
# The ordinal ω demonstrates that even-odd concepts extend to transfinite ordinals, with ω + 1 being akin to Q(Qω) = Qodd.
# With respect to the infinite input string Q(Q(...(Q))), we must distinguish between Q as a function and Q as an input.
# Q as a function (the outermost Q) behaves the opposite of H(P,P).
# We know H is a subroutine of Q, so when it passes itself into itself, we need to evaluate what H(Q,Q) does inside Q.
# Inside Q, H(Q,Q) becomes H(Qω) because we have a self-referential loop, which H evaluates as such, and then in response, the outer Q halts.
# When Q(Q) is called, H returns the state of the program at ω steps which is a loop.
# However, at ω + 1 steps, Q(Q) which becomes Q(Qω) halts, and at ω + 2 steps it loops, and so on and so forth.
# H tells us if a program(input) halts or loops forever, and Q(Q) does indeed loop forever, but it halts at forever + 1 steps.
# If we want to evaluate Q(Q(Q)) = Qω+2, we need to evaluate H(Q,Q(Q)), which when called from H within Q becomes H(Q,Qω).
# With H(Q,Qω), we have Q as the function and Qω as the input.
# Evaluating Qω would take infinite time so H(Qω) returns 'loop'.
# Evaluating H(Q,H(Qω)) = H(Q(Qω)) = H(Qω+1) = H(Qodd) = 'halt'.
# Recursively, H(Q,H(Q(Qω))) = H(Q(Q(Qω))) = H(Qω+2) = H(Qeven) = 'loop'.
# To be rigorous, we can expand out the inner H to get:
# Q(Qω)
# = H(Q,H(Qω,Qω))
# = H(Q,H(Qω(Qω)))
# = H(Q,Qω⋅2)
# = H(Q(Qω⋅2))
# = H(Qω⋅2+1)
# = H(Qodd) = 'halt'.
# Q(Q(Qω))
# = H(Q,H(Q(Qω),Q(Qω)))
# = H(Q,H(Q(Qω(Q(Qω)))))
# = H(Q,H(Q(Q1+ω(Qω))))
# = H(Q,H(Q(Qω(Qω))))
# = H(Q,H(Qω+1(Qω)))
# = H(Q(Qω⋅2+1))
# = H(Qω⋅2+2)
# = H(Qeven) = 'loop'.
# and going further, Q(Q(Q(Qω)))
# = H(Q,H(Q(Q(Qω)),Q(Q(Qω))))
# = H(Q,H(Q(Q(Qω(Q(Q(Qω)))))))
# = H(Q,H(Qω + (1 + (1 + (Qω + (1 + (1)))))))
# = H(Q,H(Qω + (1 + (1 + (Qω + (2))))))
# = H(Q,H(Qω + (1 + (1 + (Qω+2)))))
# = H(Q,H(Qω + (1 + (1 + Qω+2))))
# = H(Q,H(Qω + (1 + (Qω+2))))
# = H(Q,H(Qω + (1 + Qω+2)))
# = H(Q,H(Qω + (Qω+2)))
# = H(Q,H(Qω⋅2+2))
# = H(Q(Qω⋅2+2))
# = H(Qω⋅2+3)
# = H(Qodd) = 'halt'.
# The expressions above simplify to (Qω⋅2 + n) where n is the recursive depth of the function parameter in H.
# The inner recursive calls of the input parameter in H are absorbed into the outer Qω of the function parameter in H because 1 + ω = ω.
# With infinite recursion, we arrive at the same result because H(Q(H(Qω(...(Qω(Qω(...(Qω)))))))) = H(Q(Qω⋅2ⁿ)) = H(Qω⋅2ⁿ + 1) = H(Qodd) = 'halt'.
# With this, we see Qω = Qeven = Q(0) = Q(halt) = Q(null) loops forever, and Qω+1 = Qodd = Q(1) = Q(loop) = Q(Qω) halts completing our proof.
# Algebraically, H(x) can be modeled using the sigmoid and normalized arctan functions.
# These functions return finite values between 0 and 1, or -1 and 1 for values between -∞ and +∞.
# If we allow all program(input) strings that halt to be mapped to some hyperreal number, and all program(input) strings that loop to be mapped to +∞,
# Q(x) can be thought of as the positive domain of 1/x, where on +∞ (looping program(input)), lim x → +∞ (Q(x)) returns 0,
# on 0 (halting program(input)), lim x → 0⁺ (Q(x)) returns +∞, and in general ∀ x ∈ *ℝ, Q(x) ∈ *ℝ.
# Qn is the recursive call of Q(x) into itself = 1/(1/(1/...(1/x))), where n is the recursive depth.
# The Qn function's behavior is in direct contrast to the output of Hn-1, while Hn decides the outcome of Qn.
# We can use tan²(θ) and cot²(θ) or tan²(θ)⋅sin(θ) and cot²(θ)⋅cos(θ) to model the cyclical nature of Qn(θ).
# The functions tan²(θ) and cot²(θ) alternate between 1/x and x in the positive domain, ranging between 0 and +∞.
# The functions tan²(θ)⋅sin(θ) and cot²(θ)⋅cos(θ) alternate between 1/x and x in the positive and negative domains, ranging between -∞ and +∞.
# Together, these functions model the cyclical recursive call of Q into itself.
# We appreciate the fact that Q∞ = Qω = Qeven = Q(0) = Q(null) = Qn(0π) = Qn(2kπ) marking the beginning and end of a complete cycle.
# We can leverage limits, derivatives, and integrals on these trigonometric functions to explore the fractional and infinite recursion of Qn.
# Whether Q halts or loops when given its own code as input depends on the recursive depth of Qn, with |complex logical states| = 𝒫(ℵ₀) = 𝔠.
# This will be illustrated using the algebraic expressions defined below.
"""

# Cleaning up decimal points.
def round_to_limits(value, decimals=2):
    #Round very small values to 0 and very large values to ±∞
    if abs(value) < 1e-10:  # Threshold for considering value as 0
        return 0.0
    elif value > 1e10:  # Threshold for considering value as +∞
        return float('inf')
    elif value < -1e10:  # Threshold for considering value as -∞
        return float('-inf')
    else:
        return round(value, decimals)

# Example of a function that always halts returning 0.
def halt(x = 0, y = 0, a=1, b=1):
    # Returns 0⋅((x⋅a) + (y⋅b))
    result = 0*((x*a) + (y*b))
    return round_to_limits(result)

# Example of a function that always loops and returns ±∞.
def loop(x=0, y=0, a=1, b=1):
    # Returns +∞ for non-negative input and -∞ for negative input
    # Returns ((x⋅a) + (y⋅b))/0
    if ((x*a) + (y*b)) > 0:
        return float('inf')  # +∞ for non-negative input
    elif ((x*a) + (y*b))  < 0:
        return float('-inf')  # -∞ for negative input
    else:
        return 1 # l'Hopitals rule: lim x → 0 (sin(x)/x) = lim x → 0 (cos(x)/1)  = 1

# Definition of the function Q.
# By definition, sometimes Q halts, and sometimes it loops.
# On infinite input, it halts and returns the finite output '0'.
# On the finite input '0', it loops forever and returns infinite output.
def q_inverse(x=0, y=0, a=1, b=1):
    # Returns +∞ at 0 and 0 at +∞
    # Returns 1 / ((x⋅a) + (y⋅b))
    if (x + y) == 0:
        return float('inf')  # Return +∞ for zero input
    elif float('inf') in [x, y] or float('-inf') in [x, y]:
        # Handling division by ±∞, which results in 0
        return 0
    else:
        result = 1 / ((x*a) + (y*b))
        return round_to_limits(result)

# Definition of the function H.
# Functions for H, where it returns a yes or no answer that itself is finite, and can handle infinities as input.
def h_arctan(x=0, y=0, a=1, b=1): # Returns a number between -1 and 1
    # Returns normalized arctan(((xπ)/a) - ((yπ)/b))⋅(2/π) = arctan(θ)⋅(2/π)
    result = atan(((x)/a) - ((y)/b)) * (2 / pi)
    return round_to_limits(result)

def h_sigmoid(x=0, y=0, a=1, b=1): # Returns a number between 0 and 1
    # Returns 1/(1 + e^(-(((xπ)/a) - ((yπ)/b)))) = 1/(1 + e^(-θ))
    result = 1 / (1 + exp(-((x*a) + (y*b))))
    return round_to_limits(result)

# Functions for Qn that treat +∞ as True (loop) and 0 as halt (False).
# Here x is our starting point, and y is the integer or fractional number of recursive iterations.
# Allowing x and y to be hyperreal numbers facilitates the exploration of fractional and infinite recursion.
# Qn tan²(θ) function
def qn_tan2(x=0, y=0, a=2, b=2): # starts at 0
    # Returns tan²(((xπ)/a) - ((yπ)/b)) = tan²(θ) = recursive step # of q_inverse
    argument = ((x * pi) / a) - ((y * pi) / b)
    # Check if cos(argument) == 0, which implies cot(argument) is 0 and tan²(θ) is undefined
    if cos(argument) == 0:
        return float('inf')  # Return +∞ for tan²(θ) when cot(θ) is 0
    result = tan(argument)**2
    return round_to_limits(result)

# Qn cot²(θ) function
def qn_cot2(x=0, y=0, a=2, b=2): # starts at ∞
    # Returns cot²(((xπ)/a) - ((yπ)/b)) = cot²(θ) = recursive step # of q_inverse
    argument = ((x * pi) / a) - ((y * pi) / b)
    # Check if sin(argument) == 0, which implies tan(argument) is 0 and cot²(θ) is undefined
    if sin(argument) == 0:
        return float('inf')  # Return +∞ for cot²(θ) when tan(θ) is 0
    result = 1 / tan(argument)**2
    return round_to_limits(result)

# Functions for Qn that treat +∞ as True (loop) and -∞ as halt (False).
# Here x is our starting point, and y is the number of recursive iterations.
# Allowing x and y to be hyperreal numbers facilitates the exploration of fractional and infinite recursion.
def qn_tan2_sin(x=0, y=0, a=1, b=1): # starts at 0
    # Returns tan²(((xπ)/a)-((yπ)/b))⋅sin(((xπ)/a)-((yπ)/b)) = tan²(θ)⋅sin(θ) 
    # Calculate the argument
    argument = ((x*pi)/a) - ((y*pi)/b)
    # Check for conditions leading to ∞ directly to avoid division by zero
    if cos(argument) == 0:
        return float('inf')  # This handles the division by zero in tan²(θ) calculation
    # Calculate the expression value
    result = ((tan(argument)**2) * sin(argument))
    # Round the result to handle very small or very large values
    rounded_result = round_to_limits(result)
    return rounded_result

def qn_cot2_cos(x=0, y=0, a=1, b=1): # starts at ∞
    # Returns cot²(((xπ)/a)-((yπ)/b))⋅cos(((xπ)/a)-((yπ)/b)) = cot²(θ)⋅cos(θ)
    # Calculate the argument
    argument = ((x*pi)/a) - ((y*pi)/b)
    # Check for conditions leading to ∞ directly to avoid division by zero
    if sin(argument) == 0:
        return float('inf')  # This handles the division by zero in cot²(θ) calculation
    # Calculate the expression value
    result = ((1 / tan(argument))**2) * cos(argument)
    # Round the result to handle very small or very large values
    rounded_result = round_to_limits(result)
    return rounded_result

# Testing defs with preset constants for Qn.
# These initialize the starting point, phase shift and frequency.
# Trigonometric Qn Functions with (0 ≤ z ≤ 1)
def qn_tan2_arctan_const(x=0, y=-1, a=2, b=2):
    return qn_tan2(x, y, a, b)

def qn_cot2_arctan_const(x=0, y=0, a=2, b=2):
    return qn_cot2(x, y, a, b)

# Compositional Trigonometric Qn Functions with (0 ≤ z ≤ 1)
def qn_tan2_sin_sigmoid_const(x=0, y=-.5, a=1, b=1):
    return qn_tan2_sin(x, y, a, b)

def qn_cot2_cos_sigmoid_const(x=0, y=0, a=1, b=1):
    return qn_cot2_cos(x, y, a, b)

# Compositional Trigonometric Qn Functions with (-1 ≤ z ≤ 1)
def qn_tan2_sin_arctan_const(x=0, y=-2, a=2, b=2):
    return qn_tan2_sin(x, y, a, b)

def qn_cot2_cos_arctan_const(x=0, y=-1, a=2, b=2):
    return qn_cot2_cos(x, y, a, b)

# The Halting Machine H(Qn).
def halting_machine(x_values = [-1, 0, 1], depth = 3):
    print(f"The Halting Machine H(Qn)")
    """
    The halting_machine function explores recursive applications of H mappings (sigmoid and arctan) to three models of Qn functions.

    Our recursive Qn models operate with π radian rotations, requiring two calls to complete a full 2π cycle.
    Defining 1/x as Q, Qn effectively compresses the entire domain of 1/x, spanning the intervals (-∞, 0) and (0, ∞), into π/2 intervals.
    Through phase shifting, our trigonometric models tan²(θ) and cot²(θ) are aligned to equivalently map to the same points.
    The positive domain of the function of 1/x is compressed and mapped to the interval (2kπ, (2k + 1)π).
    The reflection about the x-axis of the negative domain of 1/x is compressed and mapped to the interval ((2k + 1)π, (2k + 2)π).
    Similarly, with phase shifting in the compositional models tan²(θ)sin(θ) and cot²(θ)cos(θ), the domain of 1/x is segmented across four intervals:
    The interval (2kπ, (2k + 1/2)π) corresponds to the positive domain of 1/x.
    The interval ((2k + 1/2)π, (2k + 1)π) corresponds to the negative domain of 1/x.
    The interval ((2k + 1)π, (2k + 3/2)π) corresponds to the reflection about the x-axis of the positive domain of 1/x.
    The interval ((2k + 3/2)π, (2k + 2)π) corresponds to the reflection about the x-axis of the negative domain of 1/x.
    Each segmentation corresponds to the positive or negative domains of 1/x and -1/x respectively, enabling a cyclical mapping of Q.

    In all models, the complete cycle encompasses a full 2π rotation, albeit scaled differently to match each model's input and output constraints.
    Each discrete recursive function call represents a rotation of π effectively spanning the entire distance of the unit circle after two recursive calls.
    Incrementing θ by additions of π/2 radians or any other angle α allows us to systematically explore its logical states.
    This mechanism allows for the investigation of complex logical dynamics by simulating continuous logical rotations.
    A complete rotation of 2π in the complex logical plane is akin to double negation '¬¬'.
    Our input argument consists of the variables x and y with constants a and b.
    The 'x' parameter represents the initial state, serving as the starting point or recursive depth of Qn.
    The 'y' parameter adjusts the phase shift responsible for the progression through logical recursive states.
    Constants 'a' and 'b' act as scaling factors, adjusting the frequency of Qn.
    The outcome of the Qn function at any given recursive step is given by Qn(θ), where θ(x,y,a,b) is the argument.

    1. ** H Arctan Trigonometric Qn Functions (0 ≤ z ≤ 1):**
    - The models, qn_tan2(θ) = tan²(xπ/a - yπ/b) and qn_cot2(θ) = cot²(xπ/a - yπ/b), showcase how arctan transitions between 0 and 1 on input between 0 and ∞.
    - The Arctan function here has a domain over the interval (0, ∞) and a range of (0 ≤ z ≤ 1).
    - Recursively applying H(Qn) creates a binary loop between 0 and 1.
    - The midpoint of x = 0.5 for Qn acts as a marker for a logical paradox consisting of our imaginary states, indicative of a system trapped between True and False.

    2. ** H Sigmoid Compositional Trigonometric Qn Functions (0 ≤ z ≤ 1):**
    - The Sigmoid Compositional models are defined as qn_tan2_sin(θ) = tan²(xπ/a - yπ/b)⋅sin(xπ/a - yπ/b) and qn_cot2_cos(θ) = cot²(xπ/a - yπ/b)⋅cos(xπ/a - yπ/b).
    - The sigmoid function here has a domain over the interval (-∞, ∞) and a range of (0 ≤ z ≤ 1).
    - Recursively applying H(Qn) creates a binary loop between 0 and 1.
    - The midpoint of x = 0.5 for Qn acts as a marker for a logical paradox consisting of our imaginary states, indicative of a system trapped between True and False.

    3. ** H Arctan Compositional Trigonometric Qn Functions (-1 ≤ z ≤ 1):**
    - The Arctan Compositional models are also defined as qn_tan2_sin(θ) = tan²(xπ/a - yπ/b)⋅sin(xπ/a - yπ/b) and qn_cot2_cos(θ) = cot²(xπ/a - yπ/b)⋅cos(xπ/a - yπ/b).
    - The Arctan function here has a domain over the interval (-∞, ∞) and a range of (-1 ≤ z ≤ 1).
    - Recursively applying H(Qn) creates a binary loop between -1 and 1.
    - The midpoint of x = 0 for Qn acts as a marker for a logical paradox consisting of our imaginary states, indicative of a system trapped between True and False.

    It is important to remember how our Qn models collapse and condense the domain of 1/x into π/2 intervals, so Qn(θ) maps an angle to some value over the entire domain of 1/x.
    In the H Arctan model, we start at x = 0 (symbolizing a halt or False state), Qn approaches +∞ which aligns with Q's base state of looping.
    When Qn is recursively applied to itself, H deciphers +∞ as 1 (indicating looping), and plugging 1 back into Q gives us 0,
    Feeding 0 back into H gives us 0 (signifying halting).
    When reintroduced back into Qn with x = 0, the function reaches ∞, which H decides as 1 (signifying looping) thus completing the cycle.
    This cycle between 0 and 1 in the positive domain of H Arctan illustrates the model's binary oscillation mapping the entire hyperreal number line onto the interval (0, 1).
    The midpoint of x = 0.5 for Qn in this model acts as the state of logical paradox, where for nπ rotations the output of H(Qn) remains 0.5.

    In the H Sigmoid Compositional model, we start at x = 0 (symbolizing a halt or False state) and Qn approaches +∞ which aligns with Q's base state of looping.
    When Qn is recursively applied to itself, H deciphers +∞ as 1 (indicating looping), and plugging 1 back into Q gives -∞.
    Feeding -∞ back into H gives us 0 (signifying halting).
    When reintroduced back into Qn with x = 0, the function reaches ∞, which H decides as 1 (signifying looping) thus completing the cycle.
    This cycle between 0 and 1 illustrates the H Sigmoid model's binary oscillation mapping the entire hyperreal number line onto the interval (0, 1).
    The midpoint of x = 0.5 for Qn in this model acts as the state of logical paradox, where for nπ rotations the output of H(Qn) remains 0.5.

    You'll recall that Q is such that it loops on a halt input and halts on a loop input.
    In the H Arctan Compositional model, we reimagine Q as a function that positively loops outputting +∞ on H's halting output '-1'.
    Here, our halting state is modeled by the negative looping output -∞ on H's looping output '+1'.
    Since our Qn has a range between ±∞ and H = (2/π)⋅arctan(x) has a range between ±1, we must alternate between +∞ at -1 and -∞ at 1.
    We phase shift left by π/2 because our base 'halt' state is -1 at -∞, and periods 0 through 3 correspond to the angles 0, π/2, π, and 3π/2 respectively.
    By phase shifting left by π/2, we effectively start at -1 where θ(x=0, y=-1, a=2, b=2) = θ(xπ/a - yπ/b) = -π/2.
    Now at x = -1 (Halting output from H), Qn approaches +∞ which aligns with Q's base state of looping.
    H deciphers +∞ as 1, and recursively reintroducing x = 1 into Qn we have θ = π/2.
    At θ = π/2, Qn reaches -∞, and feeding -∞ back into H gives us -1 (signifying halting).
    When reintroduced back into Qn with x = -1, the function reaches +∞, which H decides as 1 (signifying looping) thus completing the cycle.
    This cycle between -1 and 1 illustrates the Arctan model's binary oscillation mapping the entire hyperreal number line onto the interval (-1, 1).
    The midpoint of x = 0 for Qn in this model acts as the state of a logical paradox, where for nπ rotations the output of H(Qn) remains 0.

    For all models, if we let r = |Qn|, we can graph |Qn|⋅(e^(iθ)) in the complex plane and observe its behavior as e^(iθ) makes its way around the unit circle of complex logic.
    Using discrete recursion for Qn with each call being akin to θ+=π, if we start in a paradoxical state, such as x = 0.5 for Arctan and Sigmoid or x = 0 for Arctan Compositional models, we stay bound to the imaginary axis.
    Alternating between ±i, subsequent incrementations θ+=π maintain this anchoring, keeping Qn's hyperreal output invariably at 0.
    This value of 0 in between ±1 (True and False) symbolizes an 'undefined' or paradoxical state within the complex logic framework.
    In the complex logical plane, Qn(θ) navigates through the following critical logical states during fractional recursion:
    1 and -1 which correspond to the 'real' logical states True and False,
    while ±i denote the 'imaginary' logical states Imaginary True and Imaginary False respectively.

    # For the function Qn(θ) = tan²(θ)⋅sin(θ):
    # The derivative d/dθ(tan²(θ)⋅sin(θ)) is given by:
    # d/dθ(tan²(θ)⋅sin(θ)) = 2tan(θ)⋅(1+tan²(θ))⋅sin(θ) + tan²(θ)⋅cos(θ)
    # The integral ∫tan²(θ)⋅sin(θ)dθ is given by:
    # ∫tan²(θ)⋅sin(θ)dθ = cos(θ) + sec(θ) + C

    # For the function Qn(θ) = cot²(θ)⋅cos(θ):
    # The derivative d/dθ(cot²(θ)⋅cos(θ)) is given by:
    # d/dθ(cot²(θ)⋅cos(θ)) = -2cot(θ)⋅(1+cot²(θ))⋅cos(θ) - cot²(θ)⋅sin(θ)
    # The integral ∫cot²(θ)⋅cos(θ)dθ is given by:
    # ∫cot²(θ)⋅cos(θ)dθ = -sin(θ) - csc(θ) + C

    Graphing Qn(θ) as z = qn_cot2_cos(x=0,y=0,a=2,b=2) with z being the height above the unit circle, we see significant changes in z at multiples of π/2.
    Approaching angles 0 and π, Qn(θ) tends toward ±∞ at the points ±1 on the complex unit circle, reflecting a logical 'loop' or 'halt'.
    At π/2 and 3π/2, z tends to 0 at the points ±i reflecting imaginary looping, or imaginary halting respectively.
    The derivative d/dθ(Qn(θ)) gives us the rate of change with respect to θ (Δθ→0 and ε→0) as we approach the recursive depths at the critical points (1, i, -1, -i).
    The integral ∫Qn(θ)dθ over some periodic interval is the summation of complex logical states which averages out to 0.
    At 1 and -1 (True/False states), d/dθ(Qn(θ)) experiences sharp spikes to ±∞, signaling swift transitions to True and False states.
    At i and -i (iTrue/iFalse states) our paradoxical states, the function's rate of change levels off to 0, mirroring the logical halt in a paradox.
    If we let ρ = Qn(Θ/α, φ/β, ..., Ω/ζ), we can conceptualize higher-dimensional cyclical logic.
    Here, ρ represents the magnitude of the "truth vector" in higher-dimensional spherical space, defined as Qn evaluated at scaled angles (Θ/α, φ/β, ..., Ω/ζ).
    Variables Θ, φ, ..., Ω are the "angles of truth" in this n-dimensional logic space, and constants α, β, ..., ζ serve as scalars for these angles.
    For some variable λ we can take ∂Qn/∂λ for the partial derivative, and the gradient truth vector is ∇Qn = ⟨∂Qn/∂Θ, ∂Qn/∂φ, ..., ∂Qn/∂Ω⟩.
    We may also integrate ∫...∫(Qn)dΘ...dΩ over an n-dimensional domain in this logic vector space to explore truth densities.
    This formulation allows us to extend the concept of cyclical or periodic logic to hypercomplex numbers and into higher-dimensional spaces.
    """

    # Trigonometric models for H and Q
    functions = [
        (h_sigmoid, qn_tan2_sin_sigmoid_const, "H Sigmoid with Qn = tan²(θ)⋅sin(θ)"),
        (h_sigmoid, qn_cot2_cos_sigmoid_const, "H Sigmoid with Qn = cot²(θ)⋅cos(θ)"),
        (h_arctan, qn_tan2_arctan_const, "H Arctan with Qn = tan²(θ)"),
        (h_arctan, qn_cot2_arctan_const, "H Arctan with Qn = cot²(θ)"),
        (h_arctan, qn_tan2_sin_arctan_const, "H Arctan with Qn = tan²(θ)⋅sin(θ)"),
        (h_arctan, qn_cot2_cos_arctan_const, "H Arctan with Qn = cot²(θ)⋅cos(θ)")
    ]
    # Trigonometric recursion
    for x in x_values:
        print(f"\nEvaluating functions for x = {x}:")
        for h_func, qn_func, description in functions:
            print(f"\n{description}:")
            current_x = x
            for i in range(1, depth + 1):
                result = h_func(qn_func(current_x))
                # Print the function names and the current value of x being evaluated
                print(f"Iteration {i} with {h_func.__name__}({qn_func.__name__}({current_x})): Result = {result}")
                current_x = result
        print("")

# Complex Logic.
def complex_logic(p, q, operator, operation):
    """
    Complex Boolean variables are comprised of two components, similar to complex numbers.
    When an expression is T∧T, it is True, and when it is F∧F, it is False.
    When an expression is F∧T or T∧F, it is imaginarily True or imaginarily False respectively.
    The imaginary unit 'i' in complex analysis is essentially both half positive and half negative.
    Conceptually, for i² to equal -1, it needs to be both 1 and -1 at the same time.
    True is to 1, as False is to -1 and iTrue is to +i as iFalse is to -i.
    Mapping these on the complex plane we have [e^(i0) = 1], [e^(iπ/2) = i], [e^(iπ) = -1], and [e^(i3π/2) = -i].
    We can start with the cartesian points [1,0], [0,1], [-1,0] and [0,-1] and maintain topological equivalence after applying the transformation matrix
    T = [[√2⋅cos(π/4), -√2⋅sin(π/4)], [√2⋅sin(π/4), √2⋅cos(π/4)]] to get the cartesian points [1,1], [-1,1], [-1,-1] and [1,-1].
    We can now model the Complex Boolean Unit Vectors L = [1,1], [-1,1], [-1,-1] and [1,-1] = [T,T], [F,T], [F,F] and [T,F].
    """
    # i?(T∧T) ≡ i(T⇒T) ≡ i(F∨T) ≡ F∧T Real True to Imaginary True
    # ¬?(F∧T) ≡ ¬(F⇒T) ≡ ¬(T∨T) ≡ F∧F Imaginary True to Real False
    # i?(F∧F) ≡ i(F⇒F) ≡ i(T∨F) ≡ T∧F Real False to Imaginary False
    # ¬?(T∧F) ≡ ¬(T⇒F) ≡ ¬(F∨F) ≡ T∧T Imaginary False to Real True

    # Returns the operands and the operator
    # Introduces iNegation and iRotation to manipulate complex logical variables
    result = None
    if operation == 'inegation': # i negates only the operator
        result_p = p
        result_q = q
        result_operator =  'or' if operator == 'and' else 'and'
        result = (result_p, result_q, result_operator)
    elif operation == 'irotation': # ? negates p and the operator
        result_p = not p
        result_q = q
        result_operator =  'or' if operator == 'and' else 'and'
        result = (result_p, result_q, result_operator)
    elif operation == 'negation': # ¬ negates p, q and the operator
        result_p = not p
        result_q = not q
        result_operator =  'or' if operator == 'and' else 'and'
        result = (result_p, result_q, result_operator)
    return result

# Transitioning through all states of a 2-dimensional Complex Boolean Vector.
def complex_coinflip (coin1 = True, coin2 = True):
    print(f"Complex Coin Flip")
    p = coin1  # Initial value for p
    q = coin2  # Initial value for q
    operator = 'and'  # Initial operator for logical operations
    # Sequence of operations
    operations = ['inegation', 'irotation', 'negation', 'irotation', 'inegation', 'irotation', 'negation', 'irotation']

    # Initial print statement before operations
    print(f"operation 0/8 (starting): {(p, q, operator)}")
    # Loop through operations
    for i, operation in enumerate(operations, 1):
        result = complex_logic(p, q, operator, operation)
        print(f"operation {i}/8 ({operation}): {result}")
        p, q, operator = result  # Update p, q and operator for next iteration
    print("")  # Print a newline for separation of outputs

# Default testing def.
def test():
    x_values = [-1, 0, 1]
    depth = 3
    halting_machine(x_values, depth)
    complex_coinflip(True, True)

import sys
def blackboard(command, args): # Command line interface.
    function_map = {
        "halt": halt,
        "loop": loop,
        "q_inverse": q_inverse,
        "h_arctan": h_arctan,
        "h_sigmoid": h_sigmoid,
        "qn_tan2": qn_tan2,
        "qn_cot2": qn_cot2,
        "qn_tan2_sin": qn_tan2_sin,
        "qn_cot2_cos": qn_cot2_cos,
        "halting_machine": halting_machine,
        "complex_logic": complex_logic,
        "complex_coinflip": complex_coinflip,
    }
    func = function_map.get(command)
    if not func:
        print("Unknown command.")
        return
    prepared_args = []
    if func == halting_machine:
        # Handling for halting_machine: expects a list of numbers followed by '--' and then a depth
        if '--' not in args:
            print("Error: Missing separator '--' between x_values and depth.")
            return
        separator_index = args.index('--')
        x_values_args = args[:separator_index]  # All args before '--' are x_values
        depth_arg = args[separator_index + 1:]  # Arg after '--' is depth
        if len(depth_arg) != 1:  # Ensure exactly one argument for depth is provided
            print("Error: Please provide exactly one argument for depth after '--'.")
            return
        try:
            # Attempt to convert all x_values to float, assuming they can all be valid numbers
            x_values = [float(x) if '.' in x or 'e' in x.lower() else int(x) for x in x_values_args]
            # Depth is expected to be an integer
            depth = int(depth_arg[0])
        except ValueError as e:
            print(f"Error processing arguments for halting_machine: {e}")
            print("Ensure all x_values are valid numbers and depth is an integer.")
            return
        prepared_args = [x_values, depth]
    elif func == complex_logic:
        # Handling for complex_logic: expects two Booleans and two strings
        if len(args) >= 4:
            p, q = args[0].lower() in ['True', '1', 't', 'yes'], args[1].lower() in ['True', '1', 't', 'yes']
            operator, operation = args[2], args[3]
            prepared_args = [p, q, operator, operation]
        else:
            print("Not enough arguments for complex_logic.")
            return
    elif func == complex_coinflip:
        # Handling for complex_coinflip: expects two Booleans
        coin1 = args[0].lower() in ['True', '1', 't', 'yes'] if len(args) > 0 else None
        coin2 = args[1].lower() in ['True', '1', 't', 'yes'] if len(args) > 1 else None
        prepared_args = [coin1, coin2] if args else []
    else:
        # General handling for all other functions
        for arg in args[:4]:  # Limit to 4 arguments, accounting for specific function requirements
            if arg in ['inf', '-inf', '+inf']:
                prepared_args.append(float(arg))  # Convert 'inf', '-inf', '+inf' to float directly
            else:
                try:
                    # Attempt to convert argument to float or int based on its content
                    prepared_args.append(float(arg) if '.' in arg or 'e' in arg.lower() else int(arg))
                except ValueError:
                    print("Error: Argument type must be a float or 'inf', '-inf', '+inf'.")
                    return  # Exit function if an invalid argument is encountered
    result = func(*prepared_args)
    print(result)

def main():
    if len(sys.argv) > 1: # Call function if arguments are provided
        command = sys.argv[1]
        args = sys.argv[2:]
        blackboard(command, args)
    else:
        test()  # Default behavior if no arguments are provided

if __name__ == "__main__":
    main()