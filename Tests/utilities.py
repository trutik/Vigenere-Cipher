from vigenere import decrypt, encrypt

def base_encrypt_decrypt_test(test_object, function, message, key, expected_output):
  """
  Assert the output of an encryption/decryption is equal to the expected output for a given input.
  Base test function.
  """
  if function == decrypt:
    table = test_object.decryption_table
  elif function == encrypt:
    table = test_object.encryption_table
  else:
    raise Exception('No handling specified for function :',function.__name__)
  string = function(key, message, table, 0)
  test_object.assertEqual(string, expected_output)