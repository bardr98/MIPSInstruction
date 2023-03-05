import tkinter as tk

# Define a dictionary mapping each MIPS instruction to its properties
mips_instructions = {
    "add": {"opcode": "000000", "funct": "100000", "format": "R"},
    "addi": {"opcode": "001000", "funct": None, "format": "I"},
    "addiu": {"opcode": "001001", "funct": None, "format": "I"},
    "addu": {"opcode": "000000", "funct": "100001", "format": "R"},
    "and": {"opcode": "000000", "funct": "100100", "format": "R"},
    "andi": {"opcode": "001100", "funct": None, "format": "I"},
    "beq": {"opcode": "000100", "funct": None, "format": "I"},
    "bne": {"opcode": "000101", "funct": None, "format": "I"},
    "j": {"opcode": "000010", "funct": None, "format": "J"},
    "jal": {"opcode": "000011", "funct": None, "format": "J"},
    "jr": {"opcode": "000000", "funct": "001000", "format": "R"},
    "lui": {"opcode": "001111", "funct": None, "format": "I"},
    "lw": {"opcode": "100011", "funct": None, "format": "I"},
    "nor": {"opcode": "000000", "funct": "100111", "format": "R"},
    "or": {"opcode": "000000", "funct": "100101", "format": "R"},
    "ori": {"opcode": "001101", "funct": None, "format": "I"},
    "slt": {"opcode": "000000", "funct": "101010", "format": "R"},
    "slti": {"opcode": "001010", "funct": None, "format": "I"},
    "sltiu": {"opcode": "001011", "funct": None, "format": "I"},
    "sltu": {"opcode": "000000", "funct": "101011", "format": "R"},
    "sll": {"opcode": "000000", "funct": "000000", "format": "R"},
    "srl": {"opcode": "000000", "funct": "000010", "format": "R"},
    "sb": {"opcode": "101000", "funct": None, "format": "I"},
    "sh": {"opcode": "101001", "funct": None, "format": "I"},
    "sw": {"opcode": "101011", "funct": None, "format": "I"},
    "sub": {"opcode": "000000", "funct": "100010", "format": "R"},
    "subu": {"opcode": "000000", "funct": "100011", "format": "R"},
    "xor": {"opcode": "000000", "funct": "100110", "format": "R"},
    "xori": {"opcode": "001110", "funct": None, "format": "I"},
}


# Create a function to handle the button click event
def convert_instruction():
    # Get the user input from the text box
    instruction = instruction_entry.get().lower()

    # Check if the instruction is valid
    if instruction not in mips_instructions:
        result_label.config(text="Invalid instruction")
        return

    # Get the properties of the instruction from the dictionary
    opcode = mips_instructions[instruction]["opcode"]
    funct = mips_instructions[instruction]["funct"]
    instruction_format = mips_instructions[instruction]["format"]

    # Update the result label with the instruction properties
    result_label.config(text=f"Opcode: {opcode}\nFunct: {funct}\nFormat: {instruction_format}")


# Create a new window with a title
window = tk.Tk()
window.geometry("300x200")
window.title("MIPS Instruction Converter")

# Create a label for the instruction text box
instruction_label = tk.Label(window, text="Enter a MIPS instruction:", font=("Arial", 20))

# Create a text box for the user to enter an instruction
instruction_entry = tk.Entry(window)

# Create a button to convert the instruction
convert_button = tk.Button(window, text="Convert", command=convert_instruction, font=("Arial", 20))

# Create a label to display the result
result_label = tk.Label(window)

# Use grid layout to arrange the widgets in the window
instruction_label.grid(row=0, column=0, sticky="W")
instruction_entry.grid(row=1, column=0, padx=10, pady=5)
convert_button.grid(row=2, column=0, pady=5)
result_label.grid(row=3, column=0, padx=10, pady=5)

# Start the main event loop
window.mainloop()
