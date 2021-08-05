import pytest_pikachu.plugin

# It would be nice to replace this hardcoded constant with the pytest.ExitCode
# enum but it does not exist for Python 2.7
EXIT_CODE_OK = 0


def test_ascii_art_shown_on_successful_test_run(testdir):
    """Should show surprise if plugin enabled and test passes."""
    testdir.makepyfile("def test_passes():\n\tassert True")

    result = testdir.runpytest("--pikachu")
    result.assert_outcomes(passed=1)

    assert result.ret == EXIT_CODE_OK
    assert pytest_pikachu.plugin.ascii_art.strip() in result.stdout.str()


def test_ascii_art_not_shown_on_unless_enabled(testdir):
    """Should not show surprise if plugin is not enabled."""
    testdir.makepyfile("def test_passes():\n\tassert 1 + 1 == 2")

    result = testdir.runpytest()
    result.assert_outcomes(passed=1)

    assert result.ret == EXIT_CODE_OK
    assert pytest_pikachu.plugin.ascii_art not in result.stdout.str()


def test_ascii_art_not_shown_on_unsuccessful_test_run(testdir):
    """Should not show surprise if plugin enabled and test fails."""
    testdir.makepyfile("def test_fails():\n\tassert 1 + 1 == 3")

    result = testdir.runpytest("--pikachu")
    result.assert_outcomes(failed=1)

    assert result.ret != EXIT_CODE_OK
    assert pytest_pikachu.plugin.ascii_art not in result.stdout.str()


def test_ascii_art_not_shown_on_call_to_help(testdir):
    """Should not show surprise when the user tries to display the manual."""
    testdir.makepyfile("def test_passes():\n\tassert 1 + 1 == 2")

    result = testdir.runpytest("--pikachu", "--help")

    assert result.ret == EXIT_CODE_OK
    assert pytest_pikachu.plugin.ascii_art not in result.stdout.str()
