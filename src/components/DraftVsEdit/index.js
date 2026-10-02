import React, {useEffect, useRef, useState} from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

const IMAGE_DIR = '/img/marketing-sample/';

// A link is "real" once it is an absolute URL. Anything else (such as
// "[TODO: AI draft link]") renders as a disabled button that shows the text.
const isRealUrl = (url) => /^https?:\/\//.test(url || '');

// One labeled image. If the file is missing, shows a placeholder box instead
// of a broken-image icon, so the page lays out correctly before the
// screenshots are added.
function Shot({label, file, alt, needed}) {
  const src = useBaseUrl(`${IMAGE_DIR}${file}`);
  const imgRef = useRef(null);
  const [missing, setMissing] = useState(false);

  // onError can fire before React hydrates, so also check the loaded state.
  useEffect(() => {
    const img = imgRef.current;
    if (img && img.complete && img.naturalWidth === 0) {
      setMissing(true);
    }
  }, []);

  return (
    <figure className={styles.shot}>
      <figcaption className={styles.label}>{label}</figcaption>
      {missing ? (
        <div className={styles.placeholder} role="img" aria-label={alt}>
          <strong>Screenshot to add</strong>
          <span>{needed}</span>
          <span>
            Upload as <code>{file}</code> to <code>static{IMAGE_DIR}</code>
          </span>
        </div>
      ) : (
        <a
          href={src}
          target="_blank"
          rel="noopener noreferrer"
          className={styles.imageLink}
          title="Open full size">
          <img
            ref={imgRef}
            src={src}
            alt={alt}
            loading="lazy"
            className={styles.image}
            onError={() => setMissing(true)}
          />
        </a>
      )}
    </figure>
  );
}

function LinkButton({url, children, primary}) {
  const className = `button ${primary ? 'button--primary' : 'button--secondary'}`;
  if (!isRealUrl(url)) {
    return (
      <span className={`${className} disabled`} aria-disabled="true">
        {children} {url ? <em className={styles.todo}>{url}</em> : null}
      </span>
    );
  }
  return (
    <a className={className} href={url} target="_blank" rel="noopener noreferrer">
      {children}
    </a>
  );
}

/**
 * Side-by-side comparison of an AI draft and the edited version of one piece.
 *
 * Props:
 * - pieceName: lowercase name used in alt text, such as "landing page"
 * - brief: what was requested and who it is for
 * - draftImage / editImage: filenames in static/img/marketing-sample/
 * - draftUrl / finalUrl: optional links to the full pieces. A button shows only when its link is given
 * - children: the "What I changed and why" list, written as Markdown
 */
export default function DraftVsEdit({
  pieceName,
  brief,
  draftImage,
  editImage,
  draftUrl,
  finalUrl,
  children,
}) {
  return (
    <div className={styles.piece}>
      <p className={styles.sectionLabel}>The brief</p>
      <p>{brief}</p>

      <div className={styles.compare}>
        <Shot
          label="AI draft"
          file={draftImage}
          alt={`AI-generated draft of the Unused Access ${pieceName}, unedited`}
          needed={`The AI-generated ${pieceName}, exactly as generated.`}
        />
        <Shot
          label="My edit"
          file={editImage}
          alt={`My edited version of the Unused Access ${pieceName}`}
          needed={`The edited ${pieceName}.`}
        />
      </div>

      <p className={styles.sectionLabel}>What I changed and why</p>
      {children}

      {draftUrl || finalUrl ? (
        <div className={styles.buttons}>
          {draftUrl ? <LinkButton url={draftUrl}>Open the AI draft</LinkButton> : null}
          {finalUrl ? (
            <LinkButton url={finalUrl} primary>
              Open my final version
            </LinkButton>
          ) : null}
        </div>
      ) : null}
    </div>
  );
}
