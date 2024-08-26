import os
import importlib
import sys

def main():
    # Directory to search for functional modules
    modules_dir = 'modules'

    while True:
        # Dynamically search for functional modules
        functions = {}
        for i, filename in enumerate(os.listdir(modules_dir), start=1):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]  # Remove file extension .py
                functions[str(i)] = module_name

        print("\nPlease select a function to execute:")
        for key, value in functions.items():
            print(f"{key}: {value}")

        choice = input("Enter the function number (or 'q' to quit): ").strip()

        if choice.lower() == 'q':
            print("Exiting the program.")
            break

        if choice in functions:
            module_name = functions[choice]
            try:
                module = importlib.import_module(f"{modules_dir}.{module_name}")
                module.run()  # Call the run function in the functional module
            except ImportError:
                print(f"Unable to import module {module_name}")
            except AttributeError:
                print(f"Run function not found in module {module_name}")
        else:
            print("Invalid selection")

if __name__ == "__main__":
    main()
