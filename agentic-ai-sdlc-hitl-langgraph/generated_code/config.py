"""
Configuration file for the project.
"""

import os

class Config:
    """
    Configuration class.
    """

    def __init__(self):
        """
        Initialize the configuration.
        """
        self.spring_boot_version = "4"
        self.docker_enabled = True
        self.payment_serviceIntegrated = True
        self.admin_access = True

    def get_spring_boot_version(self):
        """
        Get the Spring Boot version.
        
        Returns:
            str: The Spring Boot version.
        """
        return self.spring_boot_version

    def is_docker_enabled(self):
        """
        Check if Docker is enabled.
        
        Returns:
            bool: True if Docker is enabled, False otherwise.
        """
        return self.docker_enabled

    def is_payment_service_integrated(self):
        """
        Check if the payment service is integrated.
        
        Returns:
            bool: True if the payment service is integrated, False otherwise.
        """
        return self.payment_serviceIntegrated

    def has_admin_access(self):
        """
        Check if the admin has access.
        
        Returns:
            bool: True if the admin has access, False otherwise.
        """
        return self.admin_access