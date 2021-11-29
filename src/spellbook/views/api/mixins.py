from collections import defaultdict


class SchoolFormatterMixin:

    @classmethod
    def reformat_school(cls, school: dict):
        spells = defaultdict(list)
        for spell in school['spells']:
            spell['spell']['schools'] = [
                {
                    'cycle': school['cycle'],
                    **school['school'],
                } for school in spell['spell']['schools']
            ]

            spell = {
                'cycle': spell['cycle'],
                **spell['spell'],
            }
            spells[f'{school["shortcut"]}{spell["cycle"]}'].append(spell)

        return {
            **school,
            'spells': spells,
        }