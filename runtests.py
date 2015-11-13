import sys
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'env_settings.settings_sqlite')

try:
    from django.conf import settings
    from django.test.utils import get_runner

    try:
        import django
        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

except ImportError:
    import traceback
    traceback.print_exc()
    raise ImportError("To fix this error, run: pip install -r requirements-test.txt")


def run_tests(*test_args):
    if not test_args:
        test_args = ['tests']

    # Run tests

    TestRunner = get_runner(settings)
    test_runner = TestRunner()

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(bool(failures))


def run_nose_tests(*test_args):
    from django_nose import NoseTestSuiteRunner

    test_runner = NoseTestSuiteRunner(test_args)

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == 'nose':
        run_nose_tests(*args[1:])
    else:
        run_tests(*args)
