package io.github.thisisthepy.pycomposeui.test.common

import kotlin.test.Test
import kotlin.test.assertTrue

class DesktopGreetingTest {

    @Test
    fun testExample() {
        assertTrue(Greeting().greet().contains("Desktop"), "Check desktop is mentioned")
    }
}
