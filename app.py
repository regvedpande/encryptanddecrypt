response = send_file(file_info['encrypted_path'], as_attachment=True, download_name=f"encrypted_{file_info['original_filename']}")

subprocess.run(['pyinstaller', '--onefile', '--noconsole', '--add-data', f'{os.path.dirname(__file__)};.', temp_wrapper, '-n', f'encrypted_{file_id}'], check=True)