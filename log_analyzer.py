def analyze_log(input_file, output_file):
    total = 0
    passed = 0
    failed = 0

    try:
        with open(input_file, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                total += 1

                if "PASS" in line:
                    passed += 1
                elif "FAIL" in line:
                    failed += 1

        success_rate = (passed / total) * 100 if total > 0 else 0

        # Writing report
        with open(output_file, 'w') as report:
            report.write("Test Execution Summary\n")
            report.write("----------------------\n")
            report.write(f"Total Tests: {total}\n")
            report.write(f"Passed: {passed}\n")
            report.write(f"Failed: {failed}\n")
            report.write(f"Success Rate: {success_rate:.2f}%\n")

        print("Report generated successfully!")
        print(f"Saved as: {output_file}")

    except FileNotFoundError:
        print("Error: Log file not found.")


analyze_log("test_log.txt", "test_report.txt")