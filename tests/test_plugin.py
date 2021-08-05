import pytest

import pytest_pikachu.plugin


def test_ascii_art_shown_on_successful_test_run(testdir: pytest.Pytester):
    """Should show surprise if plugin enabled and test passes."""
    testdir.makepyfile("def test_passes():\n\tassert True")

    result = testdir.runpytest("--pikachu")
    result.assert_outcomes(passed=1)

    assert result.ret == pytest.ExitCode.OK
    assert pytest_pikachu.plugin.ascii_art.strip() in result.stdout.str()


def test_ascii_art_not_shown_on_unless_enabled(testdir: pytest.Pytester):
    """Should not show surprise if plugin is not enabled."""
    testdir.makepyfile("def test_passes():\n\tassert 1 + 1 == 2")

    result = testdir.runpytest()
    result.assert_outcomes(passed=1)

    assert result.ret == pytest.ExitCode.OK
    assert pytest_pikachu.plugin.ascii_art not in result.stdout.str()


def test_ascii_art_not_shown_on_unsuccessful_test_run(testdir: pytest.Pytester):
    """Should not show surprise if plugin enabled and test fails."""
    testdir.makepyfile("def test_fails():\n\tassert 1 + 1 == 3")

    result = testdir.runpytest("--pikachu")
    result.assert_outcomes(failed=1)

    assert result.ret != pytest.ExitCode.OK
    assert pytest_pikachu.plugin.ascii_art not in result.stdout.str()


def test_ascii_art_not_shown_on_call_to_help(testdir: pytest.Pytester):
    """Should not show surprise when the user tries to display the manual."""
    testdir.makepyfile("def test_passes():\n\tassert 1 + 1 == 2")

    result = testdir.runpytest("--pikachu", "--help")

    assert result.ret == pytest.ExitCode.OK
    assert pytest_pikachu.plugin.ascii_art not in result.stdout.str()
