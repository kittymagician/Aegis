rule test
{
    strings:
        $test = "test"
    condition:
        any of them
}
