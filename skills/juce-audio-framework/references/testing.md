# JUCE UnitTest Framework

JUCE provides a built-in testing framework via `UnitTest` and `UnitTestRunner`. Tests are self-registering static instances that run alongside your application or in a dedicated test runner.

## Creating a Test

```cpp
#include <juce_core/juce_core.h>

class MyMathTest : public juce::UnitTest
{
public:
    MyMathTest() : juce::UnitTest ("My Math Tests", "Audio") {}

    void runTest() override
    {
        beginTest ("Addition");
        expectEquals (1 + 1, 2, "Basic addition failed");

        beginTest ("Float precision");
        expectWithinAbsoluteError (0.1f + 0.2f, 0.3f, 0.0001f,
            "Float addition precision");

        beginTest ("Range checks");
        int value = 42;
        expectGreaterThan (value, 0, "Should be positive");
        expectLessThan (value, 100, "Should be less than 100");
        expectGreaterOrEqual (value, 42, "Should be >= 42");
        expectLessOrEqual (value, 42, "Should be <= 42");

        beginTest ("Lambda test cases");
        testCase ("simple check", [this]
        {
            expect (true, "This should pass");
        });
    }
};

// Auto-register (creates a global static instance)
static MyMathTest myMathTest;
```

## Assertion Methods

```cpp
// Basic
void expect (bool result, const String& failureMessage = {});

// Equality
void expectEquals (T actual, T expected, const String& msg = {});
void expectNotEquals (T actual, T expected, const String& msg = {});

// Comparison
void expectGreaterThan (T value, T threshold, const String& msg = {});
void expectLessThan (T value, T threshold, const String& msg = {});
void expectGreaterOrEqual (T value, T threshold, const String& msg = {});
void expectLessOrEqual (T value, T threshold, const String& msg = {});

// Floating-point
void expectWithinAbsoluteError (T actual, T expected, T maxError, const String& msg = {});

// Logging
void logMessage (const String& message);

// Subsections
void beginTest (const String& testName);
void testCase (const String& name, Invokable&& testFunction);
```

## Running Tests

### Standalone Test Runner

```cpp
int main (int argc, char* argv[])
{
    juce::ScopedJuceInitialiser_GUI init;

    juce::UnitTestRunner runner;
    runner.setAssertOnFailure (false);

    // Run all tests
    for (auto* test : juce::UnitTest::getAllTests())
        runner.runTest (test);

    // Or run by category
    for (auto* test : juce::UnitTest::getTestsInCategory ("Audio"))
        runner.runTest (test);

    // Report results
    for (int i = 0; i < runner.getNumResults(); ++i)
    {
        auto* result = runner.getResult (i);
        std::cout << result->unitTestName << ": "
                  << result->failures.size() << " failures, "
                  << result->passes << " passes\n";
    }

    return runner.getNumFailures() > 0 ? 1 : 0;
}
```

### In-App Test Menu

```cpp
void runAllTests()
{
    juce::UnitTestRunner runner;
    runner.setAssertOnFailure (false);

    for (auto* test : juce::UnitTest::getAllTests())
        runner.runTest (test);

    for (int i = 0; i < runner.getNumResults(); ++i)
    {
        auto* result = runner.getResult (i);
        if (result->failures.size() > 0)
        {
            for (auto& failure : result->failures)
                DBG (failure);
        }
    }
}
```

## Querying Available Tests

```cpp
auto allTests = juce::UnitTest::getAllTests();      // Array<UnitTest*>
auto categories = juce::UnitTest::getAllCategories(); // StringArray
auto audioTests = juce::UnitTest::getTestsInCategory ("Audio");
auto namedTests = juce::UnitTest::getTestsWithName ("My Math Tests");
```

## Shared Random Number Generator

Tests share a seeded RNG for reproducibility:

```cpp
void runTest() override
{
    auto rng = getRandom();
    auto value = rng.nextFloat();  // 0.0 - 1.0
    auto intVal = rng.nextInt (100);  // 0 - 99
}
```

## Best Practices

- **Category naming**: Use consistent categories ("Audio", "DSP", "GUI", "Utils")
- **Test granularity**: Use `beginTest()` for subsections within a test class
- **Floating-point**: Always use `expectWithinAbsoluteError()` for float comparisons
- **Side effects**: Clean up in `shutdown()` override if tests modify global state
- **CI integration**: Return non-zero exit code on failures
- **Run selectively**: Use `getTestsInCategory()` to run subsets during development

## References

- JUCE UnitTest header: `modules/juce_core/unit_test/juce_UnitTest.h`
- JUCE UnitTestRunner header: `modules/juce_core/unit_test/juce_UnitTestRunner.h`
