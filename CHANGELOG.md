# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.4] - 2020-02-25

### Added
- get_user_id method added .

### Changed

- Fixed get_user problem with new style of twitter .
- joined_date, birthday, like_count removed from get_user data model due to twitter changes .


## [1.2.2] - 2020-01-04

### Changed

- Fixed tweet count bug .
- Moved from reStructured Text to MarkDown for README .
- Fixed bug in get_followers/get_followings method, which doesn't get first page tweets .

## [1.2.1] - 2019-12-23

### Added

- Search tweets with username and query string possible now .
- Filter tweets with `since` and `until` parameters in the search method .
- `__version__` property added to TwpyClient .


### Changed

- Fixed infinite loop while getting timeline .
- Improved get_timeline method .
- Fixed setup.py packages and description .



### Removed

- First request controller
