from selenium.webdriver import Chrome
import logging
import os
from definitions import ROOT_DIR


def before_all(context):
    context.logger = logging.getLogger("behave")
    context.logger.addHandler(logging.StreamHandler())


def before_feature(context, feature):
    context.logger.info(f"- Feature: {feature.name}")
    context.driver = Chrome(
        executable_path=os.path.join(ROOT_DIR, "utils", "chromedriver.exe")
    )


def after_feature(context, feature):
    context.logger.info(f"- Feature end: {feature.name}")
    context.driver.quit()


def before_scenario(context, scenario):
    context.logger.info(f"-- Scenario: {scenario.name}")


def after_scenario(context, scenario):
    context.logger.info(f"-- Scenario end: {scenario.name}")


def before_step(context, step):
    context.logger.info(f"--- Step: {step.name}")


def after_step(context, step):
    context.logger.info(f"--- Step end: {step.name}")
