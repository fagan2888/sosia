#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for nlp module."""

from nose.tools import assert_equal, assert_true
from numpy import array
from scipy.sparse import csr_matrix

from sosia.utils.nlp import clean_abstract, compute_cosine


def test_clean_abstract():
    expected = "Lorem ipsum."
    assert_equal(clean_abstract("Lorem ipsum. © dolor sit."), expected)
    assert_equal(clean_abstract("© dolor sit. Lorem ipsum."), expected)
    assert_equal(clean_abstract(expected), expected)


def test_compute_cosine():
    expected = [0.6875, 1.0625]
    received = compute_cosine(csr_matrix(array([[0.5, 0.75], [1, 0.25]])))
    assert_equal(list(received), expected)