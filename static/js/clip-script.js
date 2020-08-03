// Copy to clipboard
let flag = false;
const clipped = new ClipboardJS('#email-addr');
const doneMessage = document.querySelector('.done-text');
const completeEllipsis = document.querySelector('.add-ellipsis');
clipped.on('success', (e) => {
  const copyConfirm = document.querySelector('.copy-confirm');
  if (flag === false) {
    const ellipsis = '..';
    const doneText = ' Done!';
    completeEllipsis.textContent += ellipsis;
    doneMessage.textContent += doneText;
  }
  flag = true;
  e.clearSelection();
});