// Populate footer with current year
document.getElementById('year').innerHTML = new Date().getFullYear();
// Copy to clipboard
let flag = false;
const clipped = new ClipboardJS('#email-addr');
// const confirmationSpan = document.querySelector('.email-copied');
const doneMessage = document.querySelector('.done-text');
const completeEllipsis = document.querySelector('.add-ellipsis');
clipped.on('success', (e) => {
  const copyConfirm = document.querySelector('.copy-confirm');
  if (flag === false) {
    const ellipsis = '..';
    const doneText = ' Done!';
    // const confirmationText = ' I look forward to hearing from you!';
    completeEllipsis.textContent += ellipsis;
    doneMessage.textContent += doneText;
    // confirmationSpan.textContent += confirmationText;
  }
  flag = true;
  e.clearSelection();
});