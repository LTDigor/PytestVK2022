import pytest


class TestList:
    # multiple lists
    def test_multiple_list(self):
        l = [1] * 3
        assert len(l) == 3

    # IndexError
    def test_index_error(self):
        l = [1, 2]
        with pytest.raises(IndexError):
            assert l[3] == 0

    # type conversion
    @pytest.mark.parametrize("l, expected", [([], False), ([1], True)])
    def test_list_type(self, l, expected):
        assert bool(l) == expected


class TestTuple:
    # generate tuple
    def test_len_tuple(self):
        t = (1, 2, 3)
        assert len(t) == 3

    # TypeError
    def test_edit_tuple(self):
        t = (1, 2, 3)
        with pytest.raises(TypeError):
            t[2] = 4

    @pytest.mark.parametrize("t1, t2, expected", [((1, 2), (3,), (1, 2, 3)), ((1, 2), (), (1, 2)), ((), (), ())])
    def test_add_tuples(self, t1, t2, expected):
        assert (t1 + t2) == expected


