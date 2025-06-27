import argparse
from ai import generate_command,is_safe
from utils import execute_command

def main():
    try:
         
        parser=argparse.ArgumentParser(
            description="Convert natural language to shell commands",
            usage="%(prog)s 'your prompt' [--confirm]"
        )
        parser.add_argument(
                "prompt",
                type=str,
                help="Natural language command (e.g. 'find large files')"
        )

        parser.add_argument(
                "--confirm",
                action="store_true",
                help="Ask for confirmation before executing"
        )

        args = parser.parse_args()
        command = generate_command(args.prompt)

        print(f"🔧 Command: {command}")

        if not is_safe(command):
            print("🚨 Dangerous command blocked!")
            return
        
        if args.confirm:
                if input("Execute? [y/N] ").lower() != 'y':
                    print("Command cancelled")
                    return
                
        output = execute_command(command)
        print(f"📋 Output:\n{output}")
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
