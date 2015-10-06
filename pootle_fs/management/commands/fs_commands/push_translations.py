#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from optparse import make_option

from pootle_fs.management.commands import TranslationsSubCommand


class PushTranslationsCommand(TranslationsSubCommand):
    help = "Push translations into Pootle from FS."

    shared_option_list = (
        make_option(
            '--prune', action='store_true', dest='prune',
            help=(
                "Remove matching files that are not present as Stores in "
                "Pootle")), )
    option_list = TranslationsSubCommand.option_list + shared_option_list

    def handle(self, project_code, *args, **options):
        self.fs = self.get_fs(project_code)
        self.fs.push_translations(
            prune=options["prune"],
            fs_path=options['fs_path'], pootle_path=options['pootle_path'])