import os

class Config:
    """
    Configuration class for the application.
    """

    def __init__(self):
        self.spring_boot_version = "4"
        self.java_version = "17"
        self.mysql_version = "8"
        self.deployment_strategy = "Docker, CI/CD, cloud infrastructure"
        self.api_specifications = "RESTful APIs with JSON data format"
        self.database_design = "Relational database with tables for orders, pricing, and taxes"

    def get_spring_boot_version(self):
        """
        Returns the Spring Boot version.
        :return: str
        """
        return self.spring_boot_version

    def get_java_version(self):
        """
        Returns the Java version.
        :return: str
        """
        return self.java_version

    def get_mysql_version(self):
        """
        Returns the MySQL version.
        :return: str
        """
        return self.mysql_version

    def get_deployment_strategy(self):
        """
        Returns the deployment strategy.
        :return: str
        """
        return self.deployment_strategy

    def get_api_specifications(self):
        """
        Returns the API specifications.
        :return: str
        """
        return self.api_specifications

    def get_database_design(self):
        """
        Returns the database design.
        :return: str
        """
        return self.database_design