from unittest import TestCase

from src.core.config import AppEnvironment, AppProductionSettings, AppStagingSettings, FactoryAppSettings, get_settings


class TestSettings(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.production_settings = FactoryAppSettings(environment="production")()
        self.staging_settings = FactoryAppSettings(environment="staging")()

    def test_production_settings_initialization_successful(self):
        self.assertIsInstance(obj=self.production_settings, cls=AppProductionSettings)
        self.assertEqual(first=self.production_settings.ENVIRONMENT, second=AppEnvironment.PRODUCTION)  # type: ignore

    def test_staging_settings_initialization_successful(self):
        self.assertIsInstance(obj=self.staging_settings, cls=AppStagingSettings)
        self.assertEqual(first=self.staging_settings.ENVIRONMENT, second=AppEnvironment.STAGING)  # type: ignore

    def test_staging_settings_initialization_by_default_successful(self):
        staging_settings = get_settings()
        self.assertIsInstance(obj=staging_settings, cls=AppStagingSettings)
        self.assertEqual(first=self.staging_settings.ENVIRONMENT, second=AppEnvironment.STAGING)  # type: ignore

    def tearDown(self) -> None:
        return super().tearDown()
