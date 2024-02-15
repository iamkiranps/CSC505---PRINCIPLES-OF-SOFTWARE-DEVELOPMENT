"""
  Kiran Ponappan Sreekumari 
  CSC505 – Principles of Software Development 
  Colorado State University - Global
  Dr. Pubali Banerjee 
  February 15, 2024
  Module 1: Critical Thinking - Option #2: Umbrella Activity
  Umbrella Activities are common in the software development process. Describe the nature of these activities and develop a UML Activity Diagram to model them.
"""
class SoftwareProjectTrackingAndControl:
    def monitor_progress(self):
        print("Monitoring progress of the software project")

    def control_resources(self):
        print("Controlling resources such as budget and schedule")


class FormalTechnicalReviews:
    def conduct_review(self):
        print("Conducting formal technical reviews of software artifacts")


class SoftwareQualityAssurance:
    def define_quality_metrics(self):
        print("Defining quality metrics for the software")

    def conduct_audits(self):
        print("Conducting audits to ensure compliance with quality standards")


class SoftwareConfigurationManagement:
    def manage_versions(self):
        print("Managing versions of software artifacts")

    def control_changes(self):
        print("Controlling changes to software artifacts")


class DocumentPreparationAndProduction:
    def create_documents(self):
        print("Creating documents such as requirements and design documents")


class ReusabilityManagement:
    def identify_reusable_components(self):
        print("Identifying reusable components for future use")

    def promote_reuse(self):
        print("Promoting reuse of components across projects")


class MeasurementAndMetrics:
    def collect_data(self):
        print("Collecting data on project performance and quality metrics")

    def analyze_metrics(self):
        print("Analyzing metrics to identify areas for improvement")


class RiskManagement:
    def identify_risks(self):
        print("Identifying risks that may impact the software project")

    def mitigate_risks(self):
        print("Mitigating risks through proactive measures")


def main():
    project_tracking = SoftwareProjectTrackingAndControl()
    project_tracking.monitor_progress()
    project_tracking.control_resources()

    reviews = FormalTechnicalReviews()
    reviews.conduct_review()

    quality_assurance = SoftwareQualityAssurance()
    quality_assurance.define_quality_metrics()
    quality_assurance.conduct_audits()

    configuration_management = SoftwareConfigurationManagement()
    configuration_management.manage_versions()
    configuration_management.control_changes()

    document_production = DocumentPreparationAndProduction()
    document_production.create_documents()

    reusability_management = ReusabilityManagement()
    reusability_management.identify_reusable_components()
    reusability_management.promote_reuse()

    measurement = MeasurementAndMetrics()
    measurement.collect_data()
    measurement.analyze_metrics()

    risk_management = RiskManagement()
    risk_management.identify_risks()
    risk_management.mitigate_risks()


if __name__ == "__main__":
    main()
