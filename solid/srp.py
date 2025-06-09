# Before Refactoring
class Report:
    def generate_report(self, data):
        return f"Report based on: {data}"
    
    def format_as_pdf(self, report):
        print(f"Formatted as PDF: {report}")
    
    def email_report(self, report):
        print(f"Emailing: {report}")
    
    def process(self, data):
        report = self.generate_report(data)
        self.format_as_pdf(report)
        self.email_report(report)


# Refactored Solution
class ReportGenerator:
    def generate_report(self, data):
        return f"Report based on: {data}"


class ReportFormatter:
    def format_as_pdf(self, report):
        print(f"Formatted as PDF: {report}")


class ReportEmailer:
    def email_report(self, report):
        print(f"Emailing: {report}")


class ReportProcessor:
    def __init__(self):
        self.generator = ReportGenerator()
        self.formatter = ReportFormatter()
        self.emailer = ReportEmailer()
    
    def process(self, data):
        report = self.generator.generate_report(data)
        self.formatter.format_as_pdf(report)
        self.emailer.email_report(report)


if __name__ == "__main__":
    processor = ReportProcessor()
    processor.process("Sales Data")