import * as prompts from 'prompts';

export const prompt = (message: string) => prompts({ type: 'text', name: 'text', message });

export const confirm = () =>
  prompts({ name: '', type: 'text', message: 'Press ENTER to continue...' });

export const invalid = (message = 'INVALID COMMAND!') =>
  prompts({
    name: '',
    type: 'text',
    message: `${message} Press ENTER to continue...`
  });
