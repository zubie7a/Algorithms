# https://app.codesignal.com/company-challenges/datto/NWoHovD8M48E9Diwr
def incrementalBackups(last_backup_time, changes):
    files_to_change = {}
    # Each element of "changes" contains a timestamp and the id of a
    # file that was changed. According to the last backup time, which
    # are the files that should be backed up now?
    for change in changes:
        change_timestamp, file_id = change
        if change_timestamp > last_backup_time:
            files_to_change[file_id] = 1

    files_to_change = list(sorted(files_to_change.keys()))

    return files_to_change
