# coding=utf-8
# Author: p0psicles
#
# This file is part of Medusa.
#
# Medusa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Medusa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Medusa. If not, see <http://www.gnu.org/licenses/>.

"""Custom exceptions used or raised by imdb_api."""

__author__ = 'p0psicles'
__version__ = '1.0'

__all__ = ['ImdbException', 'ImdbError', 'ImdbUserAbort', 'ImdbShowNotFound', 'ImdbShowIncomplete',
           'ImdbSeasonNotFound', 'ImdbEpisodeNotFound', 'ImdbAttributeNotFound']


class ImdbException(Exception):
    """Any exception generated by imdb_api."""


class ImdbError(ImdbException):
    """An error with the indexer (Cannot connect, for example)."""


class ImdbUserAbort(ImdbException):
    """User aborted the interactive selection (via the q command, ^c etc)."""


class ImdbShowNotFound(ImdbException):
    """Show cannot be found on the indexer (non-existant show)."""


class ImdbShowIncomplete(ImdbException):
    """Show found but incomplete on the indexer (incomplete show)."""


class ImdbSeasonNotFound(ImdbException):
    """Season cannot be found on indexer."""


class ImdbEpisodeNotFound(ImdbException):
    """Episode cannot be found on the indexer."""


class ImdbAttributeNotFound(ImdbException):
    """Raised if an episode does not have the requested attribute (such as a episode name)."""