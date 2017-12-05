import os.path

import bolt


# DEVELOPMENT TASKS
bolt.register_task('default', [
    'pip',
    'run-unit-tests',
])
bolt.register_task('ut', [
    'run-unit-tests'
])
bolt.register_task('ct', [
    'conttest'
])

# CI/CD TASKS
bolt.register_task('execute-unit-tests', [
    'clear-pyc-testing',
    'mkdir',
    'mkdir.tests',
    'mkdir.tests.coverage',
    'nose.ci',
])

# HELPER TASKS
bolt.register_task('clear-pyc-testing',[
    'delete-pyc',
    'delete-pyc.tests',
])
bolt.register_task('clear-pyc-features', [
    'delete-pyc',
    'delete-pyc.features'
])
bolt.register_task('run-unit-tests', [
    'clear-pyc-testing',
    'nose',
])




# CONFIGURATION CONSTANTS
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(PROJECT_ROOT, 'behave_restful')
TESTS_DIR = os.path.join(PROJECT_ROOT, 'tests')
FEATURES_DIR = os.path.join(PROJECT_ROOT, 'features')
DOCS_DIR = os.path.join(PROJECT_ROOT, 'docs')
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'output')

REQUIREMENTS_FILE = os.path.join(PROJECT_ROOT, 'requirements.txt')

TESTS_RESULTS_DIR = os.path.join(OUTPUT_DIR, 'tests', 'results')
TESTS_RESULTS_FILE = os.path.join(TESTS_RESULTS_DIR, 'unit_tests_results.xml')
TESTS_COVERAGE_DIR = os.path.join(OUTPUT_DIR, 'tests', 'coverage')






config = {
    'pip': {
        'command': 'install',
        'options': {
            'r': REQUIREMENTS_FILE,
        }
    },
    'delete-pyc': {
        'sourcedir': SRC_DIR,
        'recursive': True,
        'tests': {
            'sourcedir': TESTS_DIR,
        },
        'features': {
            'sourcedir': FEATURES_DIR
        }
    },
    'nose': {
        'directory': TESTS_DIR,
        'ci': {
            'options': {
                'with-xunit': True,
                'xunit-file': TESTS_RESULTS_FILE,
                'with-coverage': True,
                'cover-erase': True,
                'cover-package': 'behave_restful',
                'cover-html-dir': TESTS_COVERAGE_DIR,
                'cover-branches': True,
            }
        }
    },
    'conttest': {
        'task': 'run-unit-tests'
    },
    'mkdir': {
        'directory': OUTPUT_DIR,
        'tests': {
            'directory': TESTS_RESULTS_DIR,
            'coverage': {
                'directory': TESTS_COVERAGE_DIR
            }
        },
    }
}