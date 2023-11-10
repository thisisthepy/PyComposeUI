from pycomposeui.runtime import Composable, EmptyComposable, ComposableTemplate

from java import jclass
import traceback

try:
    _material3 = jclass("io.github.thisisthepy.pycomposeui.Material3Kt")
    print("Compose Material3:", _material3)
    _material3_android = jclass("io.github.thisisthepy.pycomposeui.Material3_androidKt")
    print("Compose Android Material3:", _material3_android)
    _Text = _material3.TextWidget
    #Text = lambda composer, *args, **kwargs: _Text(*args, **kwargs, composer, 1)
    _SimpleText = _material3.SimpleTextWidget
    _SimpleColumn = _material3_android.SimpleColumnWidget

    @Composable
    class SimpleText(Composable):
        @classmethod
        def compose(cls, text: str = ""):
            _SimpleText(text, cls.composer, 1)

    @Composable
    class SimpleColumn(Composable):
        def compose(self, content):
            print("Hi there? ", content, self.__dict__)
            _SimpleColumn(content, self.composer, 1)

    _AnnotatedStringText = _material3.AnnotatedStringTextWidget
    #AnnotatedStringText = lambda composer, *args, **kwargs: _AnnotatedStringText(*args, **kwargs, composer, 1)
except Exception as e:
    print("-----------------------------------------------------------------------------------------------------------")
    traceback.print_exc()
    print("ERROR: PyComposeUI Material3 Library is not Found.")
    print("-----------------------------------------------------------------------------------------------------------")
    raise e
